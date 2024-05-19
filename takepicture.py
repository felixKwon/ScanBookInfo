import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os

class CameraApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")

        # 카메라 프레임
        self.camera_frame = tk.LabelFrame(root, text="Camera")
        self.camera_frame.grid(row=0, column=0, padx=10, pady=10)

        # 사진 찍기 버튼
        self.capture_button = ttk.Button(root, text="Take Picture", command=self.take_picture)
        self.capture_button.grid(row=0, column=1, padx=5, pady=10)

        # 사진 삭제 버튼
        self.delete_button = ttk.Button(root, text="Delete Picture", command=self.delete_picture)
        self.delete_button.grid(row=1, column=1, padx=5, pady=10)

         # 종료 버튼
        self.quit_button = ttk.Button(root, text="Exit", command=self.exit)
        self.quit_button.grid(row=2, column=1, padx=5, pady=10)

        # 카메라 연결
        self.cap = cv2.VideoCapture(0)
        self.is_still_image = False
        self.captured_image_filename = None  # 캡처된 이미지 파일 이름
        self.show_camera()

        root.protocol("WM_DELETE_WINDOW", self.exit)

    def show_camera(self):
        if self.is_still_image:
            return
        
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))

        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.camera_label = tk.Label(self.camera_frame, image=self.photo)
        self.camera_label.image = self.photo
        self.camera_label.grid(row=0, column=0)

        self.camera_label.after(10, self.show_camera)  # 매 10밀리초마다 카메라 프레임 업데이트

    def take_picture(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.captured_image_filename = "captured_image.jpg"
        cv2.imwrite(self.captured_image_filename, frame)
        self.is_still_image = True
        self.show_captured_image(self.captured_image_filename)
        #print("사진을 저장했습니다.")


    def show_captured_image(self, filename):
        image = Image.open(filename)
        image = image.resize((640, 480), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image=image)

        self.camera_label.config(image=photo)
        self.camera_label.image = photo

    def delete_picture(self):
        #os.remove("captured_image.jpg")
        self.captured_image_filename = None
        self.is_still_image = False
        
        self.show_camera()
        #print("사진을 삭제했습니다.")

    def exit(self):
        self.root.destroy()
        return self.captured_image_filename
    
    # 파일명을 main 에서 가져올때 사용하는 함수
    def get_captured_image_filename(self):
        return self.captured_image_filename

    def __del__(self):
        # 객체 소멸시 카메라 해제
        if hasattr(self, 'cap'):
            self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
