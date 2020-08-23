from multiprocessing import Process, current_process, Lock
import time

n = 0


def process_duty(file_name, num):
    global n
    n = n + num
    # time.sleep(2)
    n = n - num
    # time.sleep(1)
    print(n)

    with open(file_name, 'a+') as f:
        p = current_process()
        content = "process name: {} process pid: {} num: {}".format(
            p.name,
            p.pid,
            n
        )
        f.write(content)
        print(content)


class WriteProcess(Process):
    def __init__(self, num, lock,  *args, **kwargs):
        self.num = num
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        with self.lock:
            file_name = 'test_process_lock1.txt'
            for i in range(1000):
                process_duty(file_name, self.num)


if __name__ == '__main__':
    l = Lock()
    p1 = WriteProcess(5, l)
    p2 = WriteProcess(10, l)
    p1.start()
    p2.start()
    p1.join()
    p2.join()