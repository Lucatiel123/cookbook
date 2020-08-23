from multiprocessing import Process, Manager, Condition, current_process
from multiprocessing.pool import Pool
import time


def producer(q, lock, counter):
    while True:
        with lock:
            if q.full():
                print("【生产者】队列已满, 等待消费者消费")
                # 唤醒其他进程中的锁(开启其他进程中的锁)
                lock.notify_all()
                # 当前进程锁开启(暂停当前)
                lock.wait()
            else:
                item = "item{}".format(counter)
                q.put(item)
                content = "【生产者】>> 进程名为{}, 其进程id为{}， 生产编号为 {} 的物品，物品名称为 {}， 此时物品栏中物品个数为 {}". \
                    format(current_process().name, current_process().pid, counter, item, q.qsize())
                print(content)
                time.sleep(1)
                counter += 1


class consumer(Process):
    def __init__(self, q, lock, *args, **kwargs):
        self.q = q
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            with self.lock:
                if self.q.empty():
                    print("【消费者】队列已空, 等待生产者生产")
                    # 唤醒其他进程中的锁(开启其他进程中的锁)
                    self.lock.notify_all()
                    # 当前进程锁开启(暂停当前)
                    self.lock.wait()

                else:
                    item = self.q.get()
                    content = "【消费者】 << 进程名为{}, 其进程id为{}， 消费名称为 {} 的物品， 此时物品栏中物品个数为 {}". \
                        format(self.name, self.pid, item, self.q.qsize())
                    time.sleep(1)
                    print(content)


if __name__ == '__main__':
    manager = Manager()
    # 定义锁
    lock = manager.Condition()
    counter = 0
    item_basket = manager.Queue(maxsize=10)

    """
    producer_process = producer(item_basket, lock, counter)
    consumer_process = consumer(item_basket, lock)
    producer_process.start()
    consumer_process.start()
    producer_process.join()
    consumer_process.join()
    """

    p_pool = Pool(5)
    for i in range(5):
        p_pool.apply_async(producer, args=(item_basket, lock, counter,))
    p_pool.close()
    p_consumer = consumer(item_basket, lock)
    p_consumer.start()
    p_pool.join()
    p_consumer.join()
