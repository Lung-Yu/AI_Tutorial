#機器學習_ML_學習曲線

學習曲線與驗證曲線是在機器學習中很重要的兩條線，透過線的呈現可以明白模型究竟是高偏差(high bias)還是高方差(high variance)。
為什麼重要?
因為high bias and high variance在實務上的調校是不相同的!
你去對一個high bias的模型餵再多的資料，效果恐怕是有限的。
你去對一個high variance給了更多的特徵，那不是拿提汽油上場嗎?
high bias 代表 underfitting
high variance 代表 overfitting

學習來自吳恩達老師_機器學習_第六週課程
* 更多的數據
*   high variance有效
*   high bias沒效
* 嚐試用更少的特徵
*   high variance有效
* 取得更有效的特徵
*   high bias有效
* 用更高的多項式方式
*   high bias有效
*   high variance是浪費時間
* 減少正規項λ數值
*   high bias有效
* 增加正規項λ數值
*   high variance有效


# Determines cross-validated training and test scores for different training set sizes.
確定不同訓練集大小的交叉驗證訓練和測試分數。 我們可以從學習曲線了解到，我們增加了資料集之後所得的益處有多少!



從sample 1實驗中可以發現:
* 集的增加並未對模型帶來好的效果，並且這是一個高偏差的模型，調整上增加再多的模型也沒有用。 
* 圖的部份在資料集的增加情況下，是有明顯的讓驗證資料集也提升。

從sample 2實驗中可以發現:
針對訓練資料集的部份，正負了標準差之後的區域差異不大，但在驗證資料集的部份卻並非如此，這代表著這個模型有著過適的問題。

> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_%E5%AD%B8%E7%BF%92%E6%9B%B2%E7%B7%9A/842218435957190/
