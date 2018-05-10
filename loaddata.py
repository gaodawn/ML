# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:01:18 2018

@author: gaodawn
"""

# -*- coding: utf-8 -*-

import sys  
import os
import time
from numpy import *



#数据文件转矩阵
# path: 数据文件路径
# delimiter: 文件分隔符
def file2matrix(path,delimiter):	
	recordlist = []
	fp = open(path,"rb") 	# 读取文件内容
	content = fp.read()
	fp.close()
	rowlist = content.splitlines() 	# 按行转换为一维表
	# 逐行遍历
	# 结果按分隔符分割为行向量	
	recordlist =[row.split(delimiter) for row in rowlist if row.strip()]
	return mat(recordlist)	# 返回转换后的矩阵形式
	
root = "testdata" #数据文件所在路径
pathlist = os.listdir(root) # 获取路径下所有数据文件
print(pathlist)
path=root+"/"+pathlist[0]
recordlist = []
fp = open(path,"r", encoding='utf8') 	# 读取文件内容
content = fp.read()
print(content)  
fp.close()
rowlist = content.splitlines() 	# 按行转换为一维表
recordlist =[row.split("\t") for row in rowlist if row.strip()]
print(recordlist)
#for path in pathlist:
#	recordmat = file2matrix(root+"/"+path,"\t") # 文件到矩阵的转换
print(shape(recordlist)) # 输出解析后矩阵的行、列数


