# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
import numpy as np

y = np.random.randint(1,3,500)  #  亂數產生500個1跟2
scores = np.linspace(0,0.9,500)  #  產生一個0~0.9的1x500向量
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=2)
plt.plot(fpr,tpr,lw=1,label='roc')
plt.plot([0,0,1],[0,1,1],label='perfect', linestyle=':')
plt.plot([0,1],[0,1],label='judge', linestyle='--')
plt.legend()
plt.show()
