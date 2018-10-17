from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np


def loadDataSet(fileName):
    """
    函数说明:加载数据
    Parameters:
        fileName - 文件名
    Returns:
        xArr - x数据集
        yArr - y数据集
    Website:
        http://www.cuijiahua.com/
    Modify:
        2017-11-12
    """
    numFeat = len(open(fileName).readline().split('\t')) - 1
    print("numFeat:"+str(numFeat))
    xArr = []; yArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
    print(xArr)
    print(yArr)   
    return xArr, yArr
def plotDataSet():
    """
    函数说明:绘制数据集
    Parameters:
        无
    Returns:
        无

    """
    xArr, yArr = loadDataSet('ex0.txt')                                    #加载数据集
    n = len(xArr)                                                        #数据个数
    xcord = []; ycord = []                                                #样本点
    for i in range(n):                                                    
        xcord.append(xArr[i][1]); ycord.append(yArr[i])                    #样本点
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord, ycord, s = 10, c = 'blue',alpha = 0.3)                #绘制样本点
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X')
    plt.show()
if __name__ == '__main__':
    plotDataSet()