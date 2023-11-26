import tkinter as tk
import threading
import cv2
import socket
import struct
from PIL import Image, ImageTk
import pickle

HOST = 'localhost'
PORT = 8089

class VideoServer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Video Server")
        self.status_label = tk.Label(self.root, text="Server not connected", font=("Helvetica", 14))
        self.status_label.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=10)
        self.label = tk.Label(self.root)
        self.label.pack()
        self.conn = None
        self.video_thread = None
        
    def start_server(self):
        self.start_button.config(state="disabled")
        self.status_label.config(text="Waiting for connection...")
        server_thread = threading.Thread(target=self.receive_video, daemon=True)
        server_thread.start()
        
    def receive_video(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(10)
        print(f"Server listening on {HOST}:{PORT}")

        self.conn, addr = s.accept()
        print(f"Connection from {addr}")
        data = b''
        payload_size = struct.calcsize("L")
        while True:
          while len(data) < payload_size:
              data += self.conn.recv(4096)
          packed_msg_size = data[:payload_size]
          data = data[payload_size:]
          msg_size = struct.unpack("L", packed_msg_size)[0]
          while len(data) < msg_size:
              data += self.conn.recv(4096)
          frame_data = data[:msg_size]
          data = data[msg_size:]
          frame = pickle.loads(frame_data)
          # 이미지를 PhotoImage로 변환
          img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
          resized_img = resize_image(img, 200, 200)
          img_tk = ImageTk.PhotoImage(resized_img)
          # 레이블 업데이트
          self.label.configure(image=img_tk)
          self.label.image = img_tk
          #self.root.update_idletasks()  

    def update_status(self, status):
        self.status_label.config(text=status)
        if status == "Server not connected":
            self.start_button.config(state="normal")

    def run(self):
        self.root.mainloop()
    
    # 이미지 크기 조절 함수
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.ANTIALIAS)

if __name__ == '__main__':
    video_server = VideoServer()
    video_server.run()
