* 使用隨機個數樣本做群內值來適合出模型
* 把剩餘的樣本拿來測試，若數據落在定義的容許範圍內，那就加入群內值
* 使用新的群內值來適合模型
* 使用群內值來預估模型誤差
* 若誤差小於定義的容許值，或迭代次數已到定義數，即終止演算法!
* 預設scikit-learn使用MAD來估計選擇群內值，MAD代表目標變量y的絕對中位偏差。



> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_scikit-learnransacregressor/800841160094918/
