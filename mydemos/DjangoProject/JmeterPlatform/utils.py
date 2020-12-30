# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/8/13 11:05
# @File    : utils.py

from concurrent.futures import ThreadPoolExecutor
import time
import threading

lock = threading.Lock()


# 主函数1
def test1(value):
    print("func: test1 - threading: %s - values: %s" % (threading.current_thread().name, value))
    time.sleep(2)
    return 'ok'


# 主函数2
def test2(value):
    print("func: test2 - threading: %s - values: %s" % (threading.current_thread().name, value))
    time.sleep(2)
    return 'ok'


# 线程执行完成后执行的函数
def test_result(future):
    lock.acquire()
    print('future.result(): ', future.result())
    lock.release()


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix="test_") as threadPool:
        for i in range(10):
            future = threadPool.submit(test1, i)
            future.add_done_callback(test_result)

        for i in range(10):
            future = threadPool.submit(test2, i)
            future.add_done_callback(test_result)

    threadPool.shutdown(wait=True)
    print('main func finished')







