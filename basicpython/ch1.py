# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:53:24 2018

@author: gaodawn
"""

import sys  
import os
import time

# 配置utf-8输出环境


mylist = [1,2,3,4,5]
length = len(mylist)
a = 10
for indx in range(length):
	mylist[indx] = a*mylist[indx]
print (mylist)