# -*- coding: utf-8 -*-

#  Import需求lib
from __future__ import print_function

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC

print(__doc__)

# 讀入sklearn的範例資料
digits = datasets.load_digits()

#  資料預處理
# To apply an classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)  #  1797筆
X = digits.images.reshape((n_samples, -1))
y = digits.target

# 資料切割訓練與測試集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

# 要給gv的參數，可以看到正規化的惩法給了四個，gamma也給了兩個 kernel也用了rbf跟liner
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

#  評估模型的計算得分設置了兩個，並用迴圈來執行這個gv
scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()
    #  以5折下去做暴力尋參，用svc來做分類器
    clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    #  列印最佳參數
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    #  設置陣列的資料，記得參閱api
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    #  這邊依設置的參數列印出所有參數的得分狀況
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()

# Note the problem is too easy: the hyperparameter plateau is too flat and the
# output model is the same for precision and recall with ties in quality.

