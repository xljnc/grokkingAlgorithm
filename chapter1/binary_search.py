#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time      :2018/4/26 23:14
# @Author    :WuTian
# @Contact   :jsj0804wt@126.com
# @Desc

def binary_search(list, target):
    low = 0;
    high = len(list)
    while low <= high:
        mid = (low + high) / 2
        if target == list[mid]:
            return mid
        if target < list[mid]:
            high = mid - 1
        if target > list[mid]:
            low = mid + 1
    return None


my_list = [1, 3, 5, 6, 8, 11]
print(binary_search(my_list,10))
print(binary_search(my_list,5))