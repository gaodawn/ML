# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
"""
函数说明:梯度上升算法测试函数

求函数f(x) = -x^2 + 4x的极大值

Parameters:
    无
Returns:
    无
Author:

Modify:
    2017-08-28
"""
def Gradient_Ascent_test():
    def f_prime(x_old):                                    #f(x)的导数
        return -2 * x_old + 4
    x_old = -1
    xold=[]
    yold=[]
    xnew=[]
    ynew=[]                                            #初始值，给一个小于x_new的值
    x_new = 0                                            #梯度上升算法初始值，即从(0,0)开始
    alpha = 0.01                                        #步长，也就是学习速率，控制更新的幅度
    presision = 0.00000001                                #精度，也就是更新阈值
    while abs(x_new - x_old) > presision:
        x_old = x_new
        x_new = x_old + alpha * f_prime(x_old) 
        print(x_old)  
        xold.append(x_old)
        y1=-x_old*x_old + 4*x_old
        yold.append(y1)
        print(x_new)
        xnew.append(x_new)
        y2=-x_new*x_new + 4*x_old
        ynew.append(y2)
    #plotcurve(xold,yold,'red')  
    #plotcurve(xnew,ynew,'green') 
    fig = plt.figure()
    ax = fig.add_subplot(111)       #上面提到的公式
    ax.scatter(xold, yold, s = 2, c = 'red', marker = 's',alpha=.5)#绘制正样本
    ax.scatter(xnew, ynew, s = 2, c = 'green', marker = 's',alpha=.5) #绘制负样本
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X'); plt.ylabel('Y')                                    #绘制label
    plt.show()   
    print(x_new)                                        #打印最终求解的极值近似值
def plotcurve(x,y,mycolor):
    fig = plt.figure()
    ax = fig.add_subplot(111)                                         #添加subplot
    ax.scatter(x, y, s = 20, c = mycolor, marker = 's',alpha=.5)#绘制正样本
     #绘制负样本
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X'); plt.ylabel('Y')                                    #绘制label
    plt.show()                
if __name__ == '__main__':
    Gradient_Ascent_test()