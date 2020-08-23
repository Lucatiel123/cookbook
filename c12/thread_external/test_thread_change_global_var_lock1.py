import threading

import time


balance = 0
lock_k = threading.Lock()

def change(n):
    global balance

    with lock_k:
        balance = balance + n
        time.sleep(2)
        balance = balance - n
        time.sleep(1)
        print("Thread name: {} ---> var n : {} var balance : {}".format(threading.current_thread().name, balance, n))


class ChangeBalanceThread(threading.Thread):
    def __init__(self, n, *argsd, **kwargs):
        super().__init__()
        self.n = n

    def run(self):
        for i in range(10):
            change(self.n)


if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(10)
    t1.start()
    t2.start()
    t1.join()
    t2.join()