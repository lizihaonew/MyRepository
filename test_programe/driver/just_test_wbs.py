#coding:utf-8
import time

def test():
    now_time = time.time()
    a = 10
    a += 1
    b = 'test string'
    print b
    return a

x = test()
y = x + 1
print y



if __name__ == '__main__':
    test()