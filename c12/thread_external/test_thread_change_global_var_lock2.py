import threading

import time


balance = 0

lock = threading.Lock()
rlock1 = threading.RLock()
rlock2 = threading.RLock()

def change(n):
    global balance
    try:
        print("start rlock")
        rlock1.acquire()
        print("rlock1 acquire")
        rlock2.acquire()
        print("rlock2 acquire")
        balance = balance + n
        time.sleep(2)
        balance = balance - n
        time.sleep(1)
        print("Thread name: {} ---> var n : {} var balance : {}".format(threading.current_thread().name, balance, n))
    except Exception as e:
        print(e)
    finally:
        rlock1.release()
        print("rlock1 release")
        rlock2.release()
        print("rlock1 release")



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