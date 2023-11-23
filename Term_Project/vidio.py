import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import numpy as np

def update_plot(i):
    x_data = np.arange(0, 10, 0.1)
    y_data = np.sin(x_data + i * 0.1)

    ax1.clear()
    ax1.plot(x_data, y_data)
    ax1.text(0.5, 0.9, 'Subplot 1', transform=ax1.transAxes)

    ax2.clear()
    ax2.plot(x_data, y_data)
    ax2.text(0.5, 0.9, 'Subplot 2', transform=ax2.transAxes)

    ax3.clear()
    ax3.plot(x_data, y_data)
    ax3.text(0.5, 0.9, 'Subplot 3', transform=ax3.transAxes)

    canvas.draw()

# tkinter 윈도우 생성
root = tk.Tk()
root.title("Real-time Plot with Text")

# matplotlib Figure 및 Axis 생성
fig = Figure(figsize=(8, 6), dpi=100)  # figsize 매개변수로 그래프의 크기 조절
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

# 그래프를 tkinter에 추가
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 실시간 업데이트를 위한 FuncAnimation 생성
ani = FuncAnimation(fig, update_plot, interval=100)

# 그래프 간격 조절
plt.subplots_adjust(hspace=0.5)  # hspace 매개변수로 세로 간격 조절

# tkinter 메인 루프 시작
root.mainloop()