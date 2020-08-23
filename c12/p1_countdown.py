import time
from threading import Thread

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running == True:
            n -= 1
            print("T-minutes", n)
            time.sleep(3)

c = CountdownTask()
t = Thread(target=c.run, args=(5,))
t.start()

# 6s后中止线程执行
time.sleep(6)
c.terminate()
t.join()

'''
output 
T-minutes 4
T-minutes 3
'''

