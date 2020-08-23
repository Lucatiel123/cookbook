"""
  event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
  event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒；
  event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞；
  event.isSet()：判断event的标志是否为True。

"""

import threading
from time import sleep

def test_event(n, event):
    while not event.isSet():
        print("Thread %s is ready" % n)
        sleep(1)
    while event.isSet():
        print("Thread %s is running" % n)
        sleep(1)

if __name__ == '__main__':
    event = threading.Event()

    t = threading.Thread(target=test_event, args=(10, event,))
    t.start()

    event.set()