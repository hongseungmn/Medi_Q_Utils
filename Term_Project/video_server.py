# Server.py

import pickle
import socket
import struct

import cv2

HOST = 'localhost'
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('소켓 생성')

s.bind((HOST, PORT))
s.listen(10)

conn, addr = s.accept()

data = b''
payload_size = struct.calcsize("L")

while True:
    # 프레임 사이즈 측정
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    # 메시지 사이즈 기준으로 데이터 구성
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    # 프레임 로드
    frame = pickle.loads(frame_data)
    # 창으로 나타내기
    cv2.imshow('frame', frame)
    cv2.waitKey(1)