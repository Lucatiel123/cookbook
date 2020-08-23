import time
import multiprocessing
from threading import Thread


class CountdownTask(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            self.n -= 1
            print("T-minutes", self.n)
            time.sleep(3)

'''
c1 = CountdownTask(5)
c1.start()
print(c1.name)
'''

c2 = CountdownTask(5)
p = multiprocessing.Process(target=c2.run)
p.run()
print(p.name)

