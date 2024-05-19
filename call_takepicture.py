import tkinter as tk
from takepicture import CameraApp

def handle_exit(camera_app_instance):
    captured_image_filename = camera_app_instance.get_captured_image_filename()
    if captured_image_filename:
        print("사진이름은:", captured_image_filename)
    else:
        print("사진이 없어요")
    root.destroy()

def on_takepicture_exit(filename):
    if filename:
        print("사진이름은:", filename)
    else:
        print("사진이 없어요" )


if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)

    root.protocol("WM_DELETE_WINDOW", lambda: handle_exit(app))  # 창이 닫힐 때 처리할 함수 지정
    app.quit_button.config(command = lambda: handle_exit(app))

    root.mainloop()
