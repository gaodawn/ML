##示例来在官方文档，详细说明见第一个例子
import numpy as np
X = np.random.randint(10, size=(6, 100))    ##返回随机整数值：范围[0,5) 大小6*100 6行100列
y = np.array([1, 2, 3, 4, 5, 6])
z=np.random.randint(20000, size=(6, 100)) 
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)  
print(X)
print(y)
print(clf.predict(z))
from sklearn import datasets
iris = datasets.load_iris()
 
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf = clf.fit(iris.data, iris.target)
print(iris.data)
print(iris.target)
y_pred=clf.predict(iris.data)
print("高斯朴素贝叶斯，样本总数： %d 错误样本数 : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))

