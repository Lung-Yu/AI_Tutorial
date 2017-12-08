這是由國立臺灣大學所開發的。 邏輯斯迴歸能處理線性與二元分類的問題，在線性可分的情況下效能非常佳，可利用OvR技術擴展到多元分類 LogisticRegression和LogisticRegressionCV的差異在LogisticRegressionCV使用了交叉驗證來選擇正則化係數C。而LogisticRegression需要自己每次指定一個正則化係數。 除了交叉驗證，以及選擇正則化係數C以外， LogisticRegression和LogisticRegressionCV的使用方法基本相同。 邏輯斯迴歸透過了Sigmoid計算來判斷是否過門檻值，過了就是屬於那一類。


    def sigomid(z):
        return 1.0 / (1.0 + np.exp(-z)) 


> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_logisticregression/810388145806886/
