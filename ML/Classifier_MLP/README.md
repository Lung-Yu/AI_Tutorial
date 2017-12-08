這說明了，在sklearn中，MLP是利用隨機梯度或是LBFGS來做權重(參數)θθ的計算。 神經網路是最近非常熱門的一門顯學，MLP意為多層類神經網路。何謂多層，即有輸入層、輸出層跟至少一個隱藏層。

## 優缺點
### 優點：
* Capability to learn non-linear models.
* Capability to learn models in real-time (on-line learning) using partial_fit.

### 缺點：
*     MLP with hidden layers have a non-convex loss function where there exists more than one local minimum. Therefore different random weight initializations can lead to different validation accuracy.
* MLP requires tuning a number of hyperparameters such as the number of hidden neurons, layers, and iterations.
* MLP is sensitive to feature scaling.


sklearn官方說明中也提到兩個關於MLP的優點，第一點是可以學習非線性模型，第二點是可以做線上學習，所以它就會有partial_fit這個method可以使用。 缺點的部份在於，隱藏層有著non_convex的特性，所以不同的權重初始會有可能落入不同的局部最優，而非全域最優，以及MLP需調的參數很多很多，MLP對特徵縮放很敏感(記得做標準化StandardScaler(可參考官方說明搭配pipeline與gridsearchcv取alpha參數))。


> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml-mlpclassifier/826346050877762/
