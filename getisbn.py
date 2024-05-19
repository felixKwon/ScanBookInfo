import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog

# --------------------------------------------
# 바코드가 있는 사진에서 isbn을 가져온다.
# main = getisbn(): 추출된 바코드를 받아서 isbn을 추출한다.
#
#  select_files(): 파일선택창을 사용하여 사진을 선택한다
#  extract_barcode(): 사진에서 바코드를 추출한다.
# --------------------------------------------
# 파일 선택창을 사용하여 파일 선택
def select_files():
    root = tk.Tk()
    root.withdraw()  # 기본 창 숨기기

    file_paths = filedialog.askopenfilenames(title="파일 선택")

    return file_paths

# --------------------------------------------
# 사진 파일에서 바코드 가져오기
def extract_barcode(image_path):
    # 이미지 파일을 그레이스케일로 읽기
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    barcodes = decode(image)    # 이미지에서 바코드 찾기
    if len(barcodes) == 0:
        print("바코드를 찾을 수 없습니다.")
        
    return barcodes

# ---------------------------------------
# 메인 함수
def get_isbn():
    
    images = select_files() # 이미지 파일명 가져오기

    isbns = []      # isbn을 담는 list
    for image in images:    # 각각의 이미지에서
        barcodes = extract_barcode(image)  # 바코드 추출
        
        # 사진에 다수의 바코드가 있을 수 있음
        for barcode in barcodes:    
            isbn = barcode.data.decode("utf-8")
            isbns.append(isbn)

    return isbns

if __name__ == "__main__":
    get_isbn()
