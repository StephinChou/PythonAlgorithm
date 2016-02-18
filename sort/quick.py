#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-01 15:09:10
# @Author  : waitingChou (zhouzt52@qq.com)
# @Link    : https://github.com/StephinChou/
# 快速排序
import time,sortTool

arr = [13,13,47,46,23,6,38,47,49,43,9,46,26,11,15]

def log(func):
    def wrapper(*args):
        print('------')
        print(*args)

        a = func(*args)
        print(a)
        return a
    return wrapper
tmp = 0

# @log
def quickSort(data):
    length = len(data)
    # print('length',length)
    if length<=1:
        return data
    pivot,low,high = 0,0,length-1
    print('local:',data)
    while low < high:
        while low<high:
            if data[high]<data[pivot]:
                sortTool.arraySwap(data,high,pivot)
                pivot = high
                print(data)
                time.sleep(1)
                break
            high -= 1

        while low<high:
            if data[low]>data[pivot]:
                sortTool.arraySwap(data,low,pivot)
                pivot = low
                print(data)
                time.sleep(1)
                break
            low += 1
    print('-------')
    return quickSort(data[:high]) + [data[high],] + quickSort(data[high+1:])

print(quickSort(arr))
