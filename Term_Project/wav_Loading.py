import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import cv2
from micro_Stream import MicrophoneStream

# 오디오 파라미터
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# 웹캠 인자
WEBCAM_INDEX = 0  
webcam_capture = cv2.VideoCapture(WEBCAM_INDEX)



def plot_audio_and_video(audio_gen):
    full_frame = []
    CHUNK = 1024

    # 서브플롯 설정
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1,figsize=(10, 8))
    plt.subplots_adjust(hspace=0.5)  # hspace로 세로 간격 조절

    for i, x in enumerate(audio_gen):
        x = np.fromstring(x, np.int16)
        full_frame.append(x)
        str_frame = b''.join(full_frame)
        wav = np.fromstring(str_frame, np.int16)
        # 첫 번째 그래프 (상단)
        ax1.cla()
        ax1.axis([0, CHUNK * 10, -5000, 5000])
        try:
            ax1.plot(wav[-CHUNK * 10:])
        except:
            ax1.plot(wav)

        # 두 번째 그래프 (하단)
        ax2.cla()
        ax2.axis([0, CHUNK * 10, -5000, 5000])
        threshold = 2000
        wav_plot = np.clip(wav[-CHUNK * 10:], -threshold, threshold)
        ax2.plot(wav_plot, color='blue')
        # 범위를 벗어나는 값은 빨간색으로 표시
        exceed_indices = np.where(np.abs(wav[-CHUNK * 10:]) > threshold)[0]
        str_ = 'Number of Outliers : ' + str(len(exceed_indices))
        ax2.text(0.2, 0.8, str_, transform=ax2.transAxes)
        ax2.plot(exceed_indices, wav_plot[exceed_indices], 'rx')
        # 세 번째 그래프 (웹캠 영상)
        ret, frame = webcam_capture.read()
        ax3.cla()
        ax3.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ax3.axis('off')
        plt.pause(0.01)

def main():
    plt.ion()
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        plot_audio_and_video(audio_generator)
        print(list(audio_generator))

if __name__ == '__main__':
    main()
    print("end main")
