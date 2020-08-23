import time
import threading
#from multiprocessing.dummy import Pool
from concurrent.futures import ThreadPoolExecutor


def thread_run(n):
    # 线程执行的任务
    time.sleep(2)
    print('start thread "{}" duty'.format(threading.current_thread().name))
    print("the number n : {}".format(n))
    print('stop thread  "{}" duty'.format(threading.current_thread().name))


def use_Pool():
    t1 = time.time()
    list_var = range(100)
    # 使用ThreadPoolExecutor优化
    with ThreadPoolExecutor(max_workers=10) as exector:
        exector.map(thread_run, list_var)
    t2 = time.time()
    print("完成时间 {}".format(t2 - t1))


if __name__ == '__main__':
    use_Pool()