from bookinfo import get_bookinfo
from getisbn import get_isbn
import tkinter as tk
from tkinter import filedialog
import sys

# ----------------------------------------------------
def add_or_skip_listbox(lbox, newitem):
    items = lbox.get(0, tk.END)
    
    is_exist_newitem_in_items = False
    for item in items:
        if item == newitem:
            is_exist_newitem_in_items = True

    if not is_exist_newitem_in_items:
        lbox.insert(tk.END, newitem)

# ----------------------------------------------------
# info listbox 가 선택되었을 때, 아무런 액션 없음.
def info_select(event):
    return

# ----------------------------------------------------
# info listbox를 업데이트 하는 함수
def update_lbox_info(isbn):
    # yes24에서 isbn에 맞는 책 정보를 가져온다.
    bookinfos = get_bookinfo(isbn)
    # 책 정보를 기록한다. (제목, 저자, 출판다 ...)
    for bookinfo in bookinfos:
        lbox_info.insert(tk.END, bookinfo)    

# ----------------------------------------------------
# isbn listbox가 선택되었을 떼
def isbn_select(event):
    # listbox가 선택되지 않았다면 종료
    if not lbox_isbn.curselection():
        return
    
    # 선택된 isbn의 책정보를 info list박스에 기록한다.
    selected_isbn = lbox_isbn.get(lbox_isbn.curselection())
    lbox_info.delete(0, tk.END)
    update_lbox_info(selected_isbn)

# ----------------------------------------------------    
# isbn listbox를 update하는 함수
def update_lbox_isbn(isbns):
    for isbn in isbns:
        add_or_skip_listbox(lbox_isbn, isbn)

# ----------------------------------------------------
# 파일 선택 버튼이 눌러졌을 때: ISBN을 가져온다.
def listbox_isbn():
    barcodes = get_isbn()
    update_lbox_isbn(barcodes)

# ----------------------------------------------------
# 프로그램 종료 버튼이 눌러졌을 때: 윈도우를 닫고 메모리에서 제거
def close_program():
    window.destroy()
    sys.exit()

# ----------------------------------------------------
# ISBN 삭제 버튼이 눌려졌을 때: 리스트 박스를 지운다.
def listbox_isbn_delete():
    lbox_isbn.delete(0, tk.END)
    lbox_info.delete(0, tk.END)

# ----------------------------------------------------
    # 윈도우 생성
window = tk.Tk()
window.title("Book Info from YES24")

# 파일 선택 버튼
button = tk.Button(window, text="파일 선택", width=10, height=1, command = listbox_isbn)
button.grid(row=0, column=2, padx=10, pady=2)

# 리스트 삭제 버튼
btn_list_delete = tk.Button(window, text="ISBN 삭제", width=10, height=1, command = listbox_isbn_delete)
btn_list_delete.grid(row=1, column=2, padx=10, pady=2)

# 프로그램 종료 버튼
btn_close = tk.Button(window, text="프로그램 종료", width=10, height=1, command = close_program)
btn_close.grid(row=3, column=2, padx=10, pady=2)

# 창 닫을 때 호출될 함수 지정
window.protocol("WM_DELETE_WINDOW", close_program)

# 파일명을 표시할 listbox
lbox_isbn = tk.Listbox(window, width=20, height=10)
lbox_isbn.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

lbox_info = tk.Listbox(window, width=40, height=10)
lbox_info.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

# 리스트박스에서 항목 선택 이벤트 연결
lbox_isbn.bind("<<ListboxSelect>>", isbn_select)
lbox_info.bind("<<ListboxSelect>>", info_select)
# GUI 실행

window.mainloop()
# ----- 메인함수 종료 ----------------------------------
