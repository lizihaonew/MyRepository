# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/7/7 16:38
# @File    : getenv.py


# !/usr/bin/env python3

from shlex import quote
import os

JMETER_HOME = '/root/apache-jmeter-5.2.1'
CLASSPATH = os.getenv('CLASSPATH')
CLASSPATH = '%s/lib/ext/ApacheJMeter_core.jar:%s/lib/jorphan.jar:%s' % (JMETER_HOME, JMETER_HOME, CLASSPATH)
PATH = os.getenv('PATH')
PATH = '%s/bin:%s' % (JMETER_HOME, PATH)

print('export JMETER_HOME={}'.format(quote(JMETER_HOME)))
print('export CLASSPATH={}'.format(quote(CLASSPATH)))
print('export PATH={}'.format(quote(PATH)))