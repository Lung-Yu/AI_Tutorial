

極限樹是tree的一種，但是跟隨機森林一樣，都是歸類在整體學習(ensemble)中，不同於隨機森林，隨機森林在隨機產生了樹之後，那個樹會以熵為主去做樹，但極限樹，沒有極限，一切隨緣，以此方式來減少變異數(方差)。

模型的大小:O(M * N * log (N))  
M:樹的數量 
N:樣本數量 可以再搭配下列參數來控制 
min_samples_split, min_samples_leaf, max_leaf_nodes and max_depth. 

> https://www.facebook.com/notes/python-scikit-learn/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92_ml_extratreesclassifier%E6%A5%B5%E9%99%90%E6%A8%B9/808908422621525/ 
