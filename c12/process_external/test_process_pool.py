# coding: utf-8

import random
from multiprocessing import current_process, Pool
import time


def run(file_name, num):
    """
    执行业务
    往文件中写入数据
    :param file_name: str 文件民变成
    :param num: init 写入的数组
    :return: 写入的结果
    """

    with open(file_name, 'a+', encoding='utf-8') as f:
        # 当前进程
        now_process = current_process()
        # 写入内容
        content = "process name: {} process pid: {} number :{}".format(
            now_process.name,
            now_process.pid,
            num
        )
        print(content)
        f.write(content)
        f.write('\n')
        time.sleep(1)
    return 'ok'


if __name__ == '__main__':
    file_name = 'test_process_pool.txt'
    # 进程池
    pool = Pool(2)
    result_list = []
    for i in range(20):
        result = pool.apply(run, args=(file_name, i))
        # apply_async
        # result = pool.apply_async(run, args=(file_name, i))
        result_list.append(result)
        print('插入数字 {},任务执行结果 {}'.format(i, result))
    pool.close()
    pool.join()

    print(result_list)