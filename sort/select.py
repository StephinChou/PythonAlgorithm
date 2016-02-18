#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-01 15:12:16
# @Author  : waitingChou (zhouzt52@qq.com)
# @Link    : https://github.com/StephinChou/
import time
data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

for i in range(0,len(data)):
    minIndex = i
    for j in range(i,len(data)):
        if data[j] < data[minIndex]:
            minIndex = j

    tmp = data[minIndex]
    data[minIndex] = data[i]
    data[i] = tmp
    print(data)
    time.sleep(1)
print(data)



