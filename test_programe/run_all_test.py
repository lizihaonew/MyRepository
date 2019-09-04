#coding:utf-8

import unittest, time, os
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

# 指定测试用例为当前文件夹下的test_cases目录
test_dir = './mail/test_cases'
test_report = 'D:/lizihao_work/MyRepository/test_programe/mail/report'

discover = unittest.defaultTestLoader.discover(
    test_dir, pattern='*_case.py'
)

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = test_report + '/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream = fp,
        title = u'测试报告',
        description = u'运行环境：window 7， Chrome'
    )

    runner.run(discover)
    fp.close()

