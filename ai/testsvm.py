from sklearn import svm
from sklearn.externals import joblib

# Class.XXX ---相当java 的静态变量
# i > 2 and '0' or '1'  ---相当java 的i>2?0:1

X = [[i, i] for i in range(20)]  # training samples
# X = [[0, 0],[0, 0], [0, 1], [1, 0]]  # training samples

# y = [i%2 for i in range(20)]  # training target
y = [i > 2 and '0' or '1' for i in range(20)]  # training target
# y = [0,0, 1, 1]  # training target

clf = svm.SVC()  # class

clf.fit(X, y)  # training the svc model

# print(help(clf.predict))  # help

# predict the target of testing samples
# print(predict([2, 2]))
# print(predict([1, 1]))
# print(predict([3, 3]))
print(clf.predict([[i, i] for i in range(20)]))



# 保存模型
joblib.dump(clf, '../res/rf.model')

# 加载模型
RF = joblib.load('../res/rf.model')

# 应用模型进行预测
result = RF.predict([[i, i] for i in range(20)])
print("result:",result)

a = 'ad' + 'bdd' + [555].__str__()+{'k':True}.__str__()
print(a)
