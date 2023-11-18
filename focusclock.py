# 导入模块
import time
import os

# 设置工作时间和休息时间（单位为秒）
work_time = 25 * 60
break_time = 5 * 60

# 设置循环次数
cycles = 4

# 定义一个类来表示一个循环
class Cycle:
  def __init__(self, i, work_time, break_time):
    self.i = i
    self.work_time = work_time
    self.break_time = break_time

  def run(self):
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')
    # 显示当前是第几个循环
    print(f'Cycle {self.i + 1} of {cycles}')

    # 播放开始工作的声音
    os.system(f'start start.wav')

    # 等待工作时间结束
    time.sleep(self.work_time)

    # 播放开始休息的声音
    os.system(f'start break.wav')

    # 等待休息时间结束
    time.sleep(self.break_time)

    # 显示完成当前循环的提示
    print('Cycle {self.i + 1} completed.')

# 创建一个循环对象
cycle = Cycle(0, work_time, break_time)

# 循环执行所有循环
for i in range(cycles):
  cycle.run()

# 显示完成所有循环的提示
print('You have completed all cycles. Well done!')
# 播放完成所有循环的声音
os.system('start done.wav')
