# -*- coding: utf-8 -*-

# import lib
import matplotlib.pyplot as plt
#  學習曲線
from sklearn.learning_curve import learning_curve
#  驗證曲線
from sklearn.learning_curve import validation_curve
#  標準化
from sklearn.preprocessing import StandardScaler
#  標籤編碼
from sklearn.preprocessing import LabelEncoder
#  資料分集
from sklearn.cross_validation import train_test_split
#  管道
from sklearn.pipeline import Pipeline
#  logistic
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# get dateset
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',header=None)
X = df.loc[:, 2:].values
y = df.loc[:, 1].values
#  將標籤編碼
le = LabelEncoder()
#  訓練之後直接轉換
y = le.fit_transform(y)
le.transform(['M', 'B'])

#  資料拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)





#learing curl
#  設置pipeline
pipe_lr = Pipeline([
    ('scl', StandardScaler()),  #  標準化
    ('clf', LogisticRegression(  #  logistic , 正規方式為l2
                    penalty='l2', random_state=0))
])
#  訓練，learning_curve預設使用分層k折交叉驗證法
train_sizes, train_scores, test_scores = learning_curve(
                                estimator=pipe_lr,
                                X=X_train,
                                y=y_train,
                                train_sizes=np.linspace(0.1, 1.0, 10),
                                cv=10,
                                n_jobs=1)




#plot
#  訓練曲線
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
#  設置x軸是資料集，而y軸是十折的平均得分
plt.plot(train_sizes,train_mean,color='blue',marker='o',markersize=5,label='Training accuracy')
#  設置訓練曲線的均值+-標準差的區塊呈現
plt.fill_between(train_sizes,train_mean + train_std, train_mean - train_std, alpha=0.15, color='blue')
#  驗證曲線
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
#  設置x軸是資料集，而y軸是十折的平均得分
plt.plot(train_sizes,test_mean,color='green',marker='s', linestyle='--',markersize=5,label='Validation accuracy')
#  設置驗證曲線的均值+-標準差的區塊呈現
plt.fill_between(train_sizes,test_mean + test_std, test_mean - test_std, alpha=0.15, color='green')
#  設置格線
plt.grid() 
#  設置x、y軸
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
#  產生標識在右下
plt.legend(loc='lower right')
#  設置y軸間距
plt.ylim([0.8, 1.0])
plt.show()
