import threading
import time

class PerioddicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            print(self._cv)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()
        t.join()

    def wait_for_tick(self):
        """
        Wait for next tick of timer
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PerioddicTimer(5)
ptimer.start()