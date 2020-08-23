import time
import sys

count = 0

def countdown(n):
    while n > 0:
        n -= 1
        count = n
        print("T-minites: {}", n)
        time.sleep(3)


from threading import Thread
t = Thread(target=countdown, args=(5, ))
t.start()

# console
# T-minites: {} 4
# T-minites: {} 3
# T-minites: {} 2
# T-minites: {} 1
# T-minites: {} 0

if t.is_alive():
    print("running")
else:
    print("Completed")

print("t start")
# 等待该进程结束，将其连接到其他线程上
t.join()