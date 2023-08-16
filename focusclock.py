# 导入模块
import time
import os

# 设置工作时间和休息时间（单位为秒）
work_time = 25 * 60
break_time = 5 * 60

# 设置循环次数
cycles = 4

# 开始循环
for i in range(cycles):
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')
    # 显示当前是第几个循环
    print(f'Cycle {i + 1} of {cycles}')
    # 显示开始工作的提示
    print('Start working...')
    # 播放开始工作的声音（需要事先准备一个start.wav文件）
    os.system('start start.wav')
    # 等待工作时间结束
    time.sleep(work_time)
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')
    # 显示开始休息的提示
    print('Take a break...')
    # 播放开始休息的声音（需要事先准备一个break.wav文件）
    os.system('start break.wav')
    # 等待休息时间结束
    time.sleep(break_time)

# 清屏
os.system('cls' if os.name == 'nt' else 'clear')
# 显示完成所有循环的提示
print('You have completed all cycles. Well done!')
# 播放完成所有循环的声音（需要事先准备一个done.wav文件）
os.system('start done.wav')
