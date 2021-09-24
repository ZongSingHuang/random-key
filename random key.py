# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:27:25 2021

@author: zongsing.huang
"""

import numpy as np

# dim size
D = 6

# method 1

RK1 = np.random.uniform(low=0, high=D, size=[D])

# method2
RK2 = [ np.random.uniform(low=i, high=i+1) for i in range(D)]
np.random.shuffle(RK2)