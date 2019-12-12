# -*- coding: utf-8 -*-
import csv

filename = '/Users/tommy/desktop/实用脚本汇总/实名数据.csv'


with open(filename) as f:

    reader = csv.reader(f)
    for row in reader:
        print row