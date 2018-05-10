# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:21:18 2018
calculate all kinds of distances
@author: gaodawn
"""

import sys  
import os
import time
from numpy import *
import scipy.spatial.distance as dist


vector1 = mat([1,2,3])
vector2 = mat([4,7,5])

print ("欧式距离",sqrt((vector1-vector2)*((vector1-vector2).T)))

print ("曼哈顿离",sum(abs(vector1-vector2)))

print ("切比雪夫距离：",abs(vector1-vector2).max())

#计算夹角余弦
Lv1 = sqrt(vector1*vector1.T)
Lv2 = sqrt(vector2*vector2.T)
cosV12 = vector1*vector2.T/(Lv1*Lv2)
print ("余玄夹角",cosV12)
matV=mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr=nonzero(matV[0]-matV[1])
print(shape(smstr[0])[0])

Vector1 = array([1,1,0,1,0,1,0,0,1])
Vector2 = array([0,1,1,0,0,0,1,1,1])
matV = mat([Vector1 ,Vector2])
print (matV)
print ("dist.jaccard:",dist.pdist(matV,'jaccard'))
