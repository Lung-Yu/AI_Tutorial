# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.linear_model import RANSACRegressor

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header=None, sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
              'NOX', 'RM', 'AGE', 'DIS', 'RAD', 
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
#  驗證一下資料有沒有進來
df.head()

x = df[['RM']].values
y = df['MEDV'].values

from sklearn.model_selection import train_test_split
x_train,xX_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

ransac = RANSACRegressor(LinearRegression(),  #  使用的線性分類器
                         max_trials=200,  #  迭代次數
                         min_samples=200,  #  隨機個數
                         residual_metric=lambda x:np.sum(np.abs(x),axis=1),
                         residual_threshold=0.001,  #  樣本與迴歸線間的距離絕對值
                         random_state=0)
ransac.fit(x_train,  y_train) 
ransac.estimator_.coef_
ransac.estimator_.intercept_

param_trials = [200, 300]  #  設置迭代次數
param_samples = [200, 300]  #  設置隨機樣本數
param_threshold =[0.001, 0.002, 0.003]  #  設置群內值

params = []

for i in param_trials:
    for j in param_samples:
        for k in param_threshold:
            ransac = RANSACRegressor(LinearRegression(),  #  使用的線性分類器
                         max_trials=i,  #  迭代次數
                         min_samples=j,  #  隨機個數
                         residual_metric=lambda x:np.sum(np.abs(x),axis=1),
                         residual_threshold=k,  #  樣本與迴歸線間的距離絕對值
                         random_state=0)
            ransac.fit(x_train, y_train)            
            a = ransac.score(x_train, y_train)
            b = ransac.score(x_test, y_test)        
            c = ransac.estimator_.coef_[0]
            d = ransac.estimator_.intercept_
            params.append({'trials':i,
                           'samples':j,
                           'threshold':k,
                           'trainR2':a,
                           'testR2':b,
                           'coef':c,
                           'intercept':d})
import json
jp = json.dumps(params)  #  轉json
df = pd.read_json(jp)  #  讀入pandas
