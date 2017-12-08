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

from sklearn.ensemble import ExtraTreesClassifier
extra_tree = ExtraTreesClassifier(criterion='entropy',
                              n_estimators=10,
                              random_state=1,
                              n_jobs=-1)
                             
extra_tree.fit(X_train, y_train)
extra_tree.score(X_train, y_train)
extra_tree.feature_importances_  #  特徵權重
