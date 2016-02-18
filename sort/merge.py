#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-01 15:35:02
# @Author  : waitingChou (zhouzt52@qq.com)
# @Link    : https://github.com/StephinChou/
# 合并排序

import time

data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = int(len(data)/2)
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    return arrayMerge(left,right)

#算法过程装饰器
def log(func):
    def wrapper(*args):
        print('-----')
        print(*args)
        returnInfo = func(*args)
        print(returnInfo)
        time.sleep(1)
        return returnInfo
    return wrapper

@log
def arrayMerge(list1,list2):
    tmp = []
    length = len(list1)+len(list2)
    while len(tmp)<length:
        if list1 and list2:
            if list1[0]<list2[0]:
                tmp.append(list1[0])
                del list1[0]
            else:
                tmp.append(list2[0])
                del list2[0]
        else:
            tmp += list2
            tmp += list1
    return tmp



# print(arrayMerge([26, 27],[2, 46]))
print(mergeSort(data))

