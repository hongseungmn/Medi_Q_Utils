from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random, time
import threading
import pandas as pd

# CSV 파일 경로
csv_file_path = './datasets/test.csv'
# CSV 파일 읽기
df = pd.read_csv(csv_file_path)
df = df['AccX']
time_num = 0

fig = plt.figure()    
ax = plt.subplot(211, xlim=(0, 100), ylim=(0, 1024))
ax_2 = plt.subplot(212, xlim=(0, 100), ylim=(-10, 10))

max_points = 100
max_points_2 = 100
initial_values_2 = np.linspace(-10, 10, max_points_2)


line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)
line_2, = ax_2.plot(np.arange(max_points_2), 
              np.ones(max_points, dtype=np.float)*np.nan, lw=1,ms=1)

def animate(i):
  #y = ReadChannel(mcp3008_channel)
  y = random.randint(0,1000)
  old_y = line.get_ydata()
  new_y = np.r_[old_y[1:], y]
  line.set_ydata(new_y)
  #print(new_y)
  return line
    
def animate_2(i):
  global time_num
  y_2 = random.randint(0,512)
  #y_2 = df.loc[time_num]
  old_y_2 = line_2.get_ydata()
  new_y_2 = np.r_[old_y_2[1:], y_2]
  line_2.set_ydata(new_y_2)
  print(new_y_2)
  thread_1 = threading.Thread(target = testing)
  thread_1.start()
  time_num += 1
  return line_2

def testing():
  print("서브 스레드가 업무를 수행 중입니다")



anim = animation.FuncAnimation(fig, animate ,interval = 200)
anim_2 = animation.FuncAnimation(fig, animate_2  , interval=200)
plt.show()
