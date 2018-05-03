#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: WuTian
# @Date  : 2018/5/3
# @Contact : jsj0804wt@126.com
# @Desc  : 使用Dijkstra算法


def find_lowest_cost(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs)
    while node is not None:
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = costs[node] + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def get_path(parents, name):
    path = name
    while name in parents:
        path += ("->" + parents[name])
        name = parents[name]
    return path


graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["a"] = 2
graph["a"] = {}
graph["a"]["final"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 5
graph["final"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["final"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None

processed = []

find_lowest_cost(graph, costs, parents, processed)
print costs["final"]
print get_path(parents, "final")
