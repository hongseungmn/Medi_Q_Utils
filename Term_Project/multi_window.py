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
        self.clients = []  # 연결된 클라이언트를 저장하는 리스트

    def start_server(self):
        self.start_button.config(state="disabled")
        self.status_label.config(text="Waiting for connection...")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(10)

        # 새로운 쓰레드에서 클라이언트 연결을 기다림
        server_thread = threading.Thread(target=self.accept_clients, args=(server_socket,))
        server_thread.start()

    def accept_clients(self, server_socket):
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            client_label = tk.Label(self.root)
            client_label.pack()
            video_stream = VideoStream(client_socket, client_label)
            client_thread = threading.Thread(target=video_stream.receive_video, daemon=True)
            client_thread.start()
            self.clients.append((client_label, video_stream))

    def run(self):
        self.root.mainloop()

class VideoStream:
    def __init__(self, socket, label):
        self.socket = socket
        self.label = label

    def receive_video(self):
        data = b''
        payload_size = struct.calcsize("L")
        while True:
            while len(data) < payload_size:
                data += self.socket.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            resized_img = resize_image(img, 200, 200)
            img_tk = ImageTk.PhotoImage(resized_img)
            self.label.configure(image=img_tk)
            self.label.image = img_tk
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.ANTIALIAS)

if __name__ == '__main__':
    video_server = VideoServer()
    video_server.run()
