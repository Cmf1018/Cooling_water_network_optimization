#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/26 10:57
# @Author : Haoyu Miao
# @File : cwno_network.py
# @Software: PyCharm

import networkx
import cwno_components

# valve_1 = cwno_components.Valve(flow=1)
#
# valve_1.compute_pressure()
#
# print(valve_1.pressure)

class CWNONetwork(networkx.DiGraph):
    def __init__(self):
        super(CWNONetwork, self).__init__()

    def example_method(self):
        print("Chao ge hao shuai!")

