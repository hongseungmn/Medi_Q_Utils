# client.py

import cv2
import numpy as np
import socket
import sys
import pickle
import struct

# 비디오 경로 읽어오기
cap=cv2.VideoCapture(0)

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))

while True:
    ret,frame=cap.read()

	# 프레임 직렬화하여 전송준비
    data = pickle.dumps(frame)

    # 메시지 길이 측정
    message_size = struct.pack("L", len(data))

    # 데이터 전송
    clientsocket.sendall(message_size + data)