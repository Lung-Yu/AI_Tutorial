# -*- coding: utf-8 -*-

#  取得資料
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

#  資料分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(
X, y, test_size=0.3, random_state=0)

#  資料標準化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

#  載入邏輯斯迴歸
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1000.0,
                        random_state=0)
lr.fit(X_train_std, y_train)                        

lr.predict_proba(X_test_std)  #  回傳各特徵的各目標標籤的機率

