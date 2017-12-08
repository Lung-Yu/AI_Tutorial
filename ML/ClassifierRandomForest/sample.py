# -*- coding: utf-8 -*-

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

#  如果是2.0版的話,from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(
X, y, test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(criterion='entropy',
                              n_estimators=10,
                              random_state=1,
                              n_jobs=-1)
                              #  記得上面的備註嗎?多數會用預設的參數。
                              #  定義要產生的樹，定義使用的CPU跟熵或GINI就夠了!
forest.fit(X_train, y_train)
forest.score(X_train, y_train)
forest.feature_importances_  #  特徵權重

