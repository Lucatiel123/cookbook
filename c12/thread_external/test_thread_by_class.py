import threading
import time


def loop(n):
    while n > 0:
        print("Thread name {}",format(threading.current_thread().name))
        print(n)
        time.sleep(2)
        n -= 1


class LoopThread(threading.Thread):
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = n

    def run(self):
        loop(self.n)


if __name__ == '__main__':
    print("Now thread name:")
    print(threading.current_thread().name)
    t = LoopThread(5, name="Loop thread")
    t.start()
    t.join()