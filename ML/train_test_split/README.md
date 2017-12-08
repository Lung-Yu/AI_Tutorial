x:特徵資料集 
y:目標資料集 
test_size=0.3:代表切了3成去做測試數據集! 
random_state:亂數種子，每次設置一樣所得亂數相同! 

    import pandas as pd
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header=None, sep='\s+')
    
    df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
                  'NOX', 'RM', 'AGE', 'DIS', 'RAD', 
                  'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    #  驗證一下資料有沒有進來
    df.head()
    
    x = df[['RM']].values
    y = df['MEDV'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.3, 
                                                        random_state=0)

> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_train_test_split/806567659522268/
