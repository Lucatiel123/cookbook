import time
import threading
from multiprocessing.dummy import Pool


def thread_run(n):
    # 线程执行的任务
    time.sleep(2)
    print('start thread "{}" duty'.format(threading.current_thread().name))
    print("the number n : {}".format(n))
    print('stop thread  "{}" duty'.format(threading.current_thread().name))


def use_Pool():
    t1 = time.time()
    pool = Pool(10)
    list_var = range(100)
    pool.map(thread_run, list_var)
    pool.close()
    pool.join()
    t2 = time.time()
    print("完成时间 {}".format(t2 - t1))

if __name__ == '__main__':
    use_Pool()