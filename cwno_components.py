#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/26 10:53
# @Author : Haoyu Miao
# @File : cwno_components.py
# @Software: PyCharm

class Pipe:
    def __init__(self):
        pass

    def compute_pressure(self):
        pass


class Valve:
    def __init__(self, flow):
        self.flow = flow
        self.pressure = None

    def compute_pressure(self):
        self.pressure = self.flow ** 2 + 3 * self.flow



class HeatExchanger:
    def __init__(self):
        pass

    def compute_pressure(self):
        pass