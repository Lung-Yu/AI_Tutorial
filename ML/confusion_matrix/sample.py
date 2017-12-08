from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
y_true = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0 ,1]
y_pred = [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1 ,1]
confmat = confusion_matrix(y_true=y_true, y_pred=y_pred)
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i,j], va='center', ha='center')
plt.xlabel('predicted label')        
plt.ylabel('true label')
plt.show()
