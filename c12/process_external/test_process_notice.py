from multiprocessing import Process, Queue, current_process
import random
import time


class Write(Process):
    def __init__(self, queue, *args, **kwargs):
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        content = [
            "line1",
            "line2",
            "line3",
            "line4"
        ]
        for line in content:
            print("in process {}, write {} to Queue".format(current_process().name, line))
            self.queue.put(line)

            time.sleep(1)

class Read(Process):
    def __init__(self, queue, *args, **kwargs):
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            content = self.queue.get()
            print("in process {}, get {} from Queue".format(current_process().name, content))


if __name__ == '__main__':
    q = Queue()
    print("启动写进程")
    p1 = Write(q)
    p1.start()
    print("启动读进程")
    p2 = Read(q)
    p2.start()

    print("p1-join before")
    # p1进程停止之前代码会停止在 p1.join()
    p1.join()
    print("p1-join after")
    if q.empty():
        # p2强制停止
        p2.terminate()