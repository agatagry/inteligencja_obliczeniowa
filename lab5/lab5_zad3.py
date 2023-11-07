import numpy
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from sklearn import tree
# iris = load_iris()
# X, y = iris.data, iris.target
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)

# print(X, y)
df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=292753)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
print(dtc.score(test_inputs, test_classes))
prediction = dtc.predict(test_inputs)
print(confusion_matrix(test_classes, prediction))


tree.plot_tree(dtc)
plt.show()
