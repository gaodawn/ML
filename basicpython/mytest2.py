# -*- coding: utf-8 -*-

import sys  
import os
import time
import numpy



mylist = [1,2,3,4,5]
length = len(mylist)
a = 10
for indx in range(length):
	mylist[indx] = a*mylist[indx]
print (mylist)

