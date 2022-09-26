#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/26 11:00
# @Author : Haoyu Miao
# @File : cwno_model.py
# @Software: PyCharm

from cwno_network import CWNONetwork

class CWNOModel():
    def __init__(self):
        pass

    def construct_cwno_network(self):
        network = CWNONetwork()
        return network

    def solve(self):
        network = self.construct_cwno_network()
        network.example_method()

