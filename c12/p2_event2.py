"""
  event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
  event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒；
  event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞；
  event.isSet()：判断event的标志是否为True。
"""

# 如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。

from threading import Thread, Event
import time


def countdown(n, started_event):
    print("countdown thread start")
    started_event.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(3)


start_event = Event()

print("launching countdown")
t = Thread(target=countdown, args=(10, start_event))
t.start()


start_event.wait()
print("countdown thread is running")