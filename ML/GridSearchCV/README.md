Exhaustive search over specified parameter values for an estimator. 開宗明義的一句話，就是極盡所能的對所有指定的參數做搜尋，故稱之為暴力搜尋。 透過GridSearchCV我們可以對所設置的所有參數做所有的可能排列組合下去測，然後取得一個最佳參數。相對的，這部份的取得成本是非常可觀的。 個人用了50k筆資料，測了幾個條件去做，印象中是跑了5小時才結束… Important members are fit, predict. 重點是模型要有fit跟predict這兩個方法!! 也可以搭配著pipeline來執行，就不用另外再做個標準化或pca的動作，讓pipeline來處理就可以。

> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_gridsearchcv_%E7%B6%B2%E6%A0%BC%E6%90%9C%E5%B0%8B/812823088896725/
