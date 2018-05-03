#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: WuTian
# @Date  : 2018/5/3
# @Contact : jsj0804wt@126.com
# @Desc  :使用广度优先搜索查找芒果商
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_mango_seller(name):
    return name[-1] == "m"


def search_mango_seller(name):
    search_queue = deque()
    searched = []
    global graph
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                print("%s is a mango seller" % person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search_mango_seller("you")
