#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-01 15:19:14
# @Author  : waitingChou (zhouzt52@qq.com)
# @Link    : https://github.com/StephinChou/
import time

data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

length = len(data)

for i in range(0,length):
    for j in range(0,i):
        if data[j] > data[i]:
            tmp = data[j]
            data[j] = data[i]
            data[i] = tmp
    print(data)
    time.sleep(1)
print(data)
