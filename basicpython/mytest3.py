# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:57:43 2018

@author: gaodawn
"""

import sys  
import os
import time
import numpy as np 

# 配置utf-8输出环境


mylist = [1,2,3,4,5,6,7,8,9,10]
a = 10
mymatrix = np.mat(mylist)
print (a*mymatrix)