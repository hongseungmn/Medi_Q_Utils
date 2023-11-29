import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import cv2
import librosa.display
from micro_Stream import MicrophoneStream
import threading
import socket
import pickle
import struct

# 오디오 파라미터
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# 데이터 전송 플래스
FLAG = False

# 웹캠 인자
WEBCAM_INDEX = 0  
webcam_capture = cv2.VideoCapture(WEBCAM_INDEX)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))


def plot_audio_and_mel_spectrogram(audio_gen):
    global FLAG
    full_frame = []
    CHUNK = 1024

    # 서브플롯 설정
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.5)
    thread_1 = threading.Thread(target = streaming)
    thread_1.start()
    for i, x in enumerate(audio_gen):
        x = np.frombuffer(x, np.int16)
        full_frame.append(x)
        str_frame = b''.join(full_frame)
        wav = np.frombuffer(str_frame, np.int16)

        # 첫 번째 그래프 (상단 - 기본)
        ax1.cla()
        ax1.axis([0, CHUNK * 10, -8000, 8000])
        try:
            ax1.plot(wav[-CHUNK * 10:])
        except:
            ax1.plot(wav)

        # 두 번째 그래프 (하단, mel-spectrogram)
        ax2.cla()
        # 여기에서 원하는 y 축의 범위를 지정
        y_axis_range = [-20, 20000]
        ax2.axis([0, CHUNK/100, y_axis_range[0], y_axis_range[1]])
        try:
            mel_spectrogram = librosa.feature.melspectrogram(y=wav[-CHUNK * 230:].astype(float), sr=RATE, n_fft=1600)
            display_data = librosa.power_to_db(mel_spectrogram, ref=np.max)
            # print('display_data : ',display_data)
            librosa.display.specshow(display_data, y_axis='mel', x_axis='time', ax=ax2)
        except Exception as e:
            print(f"Error during spectrogram calculation: {e}")
        
        # 세 번째 그래프 (웹캠 영상)
        # ret, frame = webcam_capture.read()
        # ax3.cla()
        # ax3.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # ax3.axis('off')
        
        # 네 번째 그래프 (이상치 탐지)
        ax3.cla()
        ax3.axis([0, CHUNK * 10, -8000, 8000])
        threshold = 5000
        wav_plot = np.clip(wav[-CHUNK * 10:], -threshold, threshold)
        ax3.plot(wav_plot, color='blue')
        # 범위를 벗어나는 값은 빨간색으로 표시
        exceed_indices = np.where(np.abs(wav[-CHUNK * 10:]) > threshold)[0]
        str_ = 'Number of Outliers : ' + str(len(exceed_indices))
        ax3.text(0.2, 0.8, str_, transform=ax3.transAxes)
        ax3.plot(exceed_indices, wav_plot[exceed_indices], 'rx')
        if (len(exceed_indices) >= 1000) and thread_1.is_alive():
            print("이상치 탐지됨")
            FLAG = True
        else:
            FLAG = False
        plt.pause(0.01)

def streaming():
    # 비디오 경로 읽어오기
    while True:
        ret,frame=webcam_capture.read()
        # 프레임 직렬화하여 전송준비
        # 이미지 데이터와 추가 데이터를 함께 전송
        additional_data = ''
        if FLAG:
            additional_data = "1번기계에서 결함 발견"
            # 이미지 데이터와 추가 데이터를 함께 전송
        data = pickle.dumps((frame, additional_data))
        # data = pickle.dumps(frame)
        # data = pickle.dumps(frame)
        # 메시지 길이 측정
        message_size = struct.pack("L", len(data))
        # 데이터 전송
        clientsocket.sendall(message_size + data)

def main():
    plt.ion()
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        plot_audio_and_mel_spectrogram(audio_generator)
        print(list(audio_generator))

if __name__ == '__main__':
    main()
    print("end main")
