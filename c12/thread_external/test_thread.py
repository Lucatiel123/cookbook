import threading
import time


def loop(n):
    while n > 0:
        print("Thread name {}",format(threading.current_thread().name))
        print(n)
        time.sleep(2)
        n -= 1


if __name__ == '__main__':
    this_thread_name = threading.current_thread().name
    print("main thread name : {}".format(this_thread_name))
    t = threading.Thread(target=loop, args=(5,), name="loop-thread")
    t.start()
    t.join()