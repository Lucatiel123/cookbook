import os
import time
from multiprocessing import Process, current_process


def process_duty(name):
    """
    进程的执行任务
    :param name: 进程的名称
    :return:
    """
    print("Process name: {} , process PID: {}".format(name, os.getpid()))
    time.sleep(5)


class Process_A(Process):

    def __init__(self, name, *args, **kwargs):
        self.process_name = name
        super().__init__(*args, **kwargs)

    def run(self):
        # run方法中已经是一个进程了
        print("Process A's name is {}, pid is {}".format(self.process_name, os.getpid()))
        print("Process_A 执行任务，然后调起其他进程")
        # 接收 name="Process A" 参数
        process_duty(self.process_name)
        # 接收 args=("Process B",) 参数
        super().run()
        time.sleep(5)


if __name__ == '__main__':
    p = Process_A(target=process_duty, args=("Process B",), name="Process A")
    p.start()
    p.join()