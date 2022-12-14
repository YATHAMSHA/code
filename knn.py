from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import seaborn as sn

data  = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

X_train,X_test,Y_train,Y_test = train_test_split(np.array(data.data),np.array(data.target),test_size=0.2)

from sklearn import neighbors
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,Y_train)

print(clf.score(X_test,Y_test))

predictions = clf.predict(X_test)
Confusion_matrix = confusion_matrix(Y_test,predictions)
sn.heatmap(Confusion_matrix,annot = True)
