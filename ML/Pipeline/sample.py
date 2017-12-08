# -*- coding: utf-8 -*-

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import codecs
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

df = pd.DataFrame()
path = 'D:\\ML\\movie_data.csv'
porter = PorterStemmer()
stop = stopwords.words('english')

#  目前很常遇到的就是編碼的問題，所以最後找到的解法是import codecs再透過with codecs來oepn。
with codecs.open(path, "r", encoding='utf-8', errors='ignore') as fdata:
    df = pd.read_csv(fdata)


x_train = df.loc[:50, 'review'].values
y_train = df.loc[:50, 'sentiment'].values
#  上面是訓練資料，下面是測試資料
x_test = df.loc[50:, 'review'].values
y_test = df.loc[50:, 'sentiment'].values


tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None
                        )

#  透過pipeline執行的時候，最後一個一定是模型!
lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=0))])


print(lr_tfidf.fit(x_train, y_train))
#  利用訓練資料驗證可靠度
print(lr_tfidf.score(x_test, y_test))
