#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time      :2018/5/1 23:05
# @Author    :WuTian
# @Contact   :jsj0804wt@126.com
# @Desc

from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


intArray = []
for x in range(9):
    intArray.append(randint(1, 99))

print(quick_sort(intArray))
