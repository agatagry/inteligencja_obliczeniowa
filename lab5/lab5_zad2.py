import numpy
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=292753)


def classify_iris(sl, sw, pl, pw):
    if pl < 2:
        return "Setosa"
    elif pl > 4.5:
        return "Virginica"
    else:
        return "Versicolor"


good_preconditions = 0
length = test_set.shape[0]

for i in range(length):
    if classify_iris(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3]) == test_set[i, 4]:
        good_preconditions = good_preconditions + 1

print(good_preconditions)
print(good_preconditions / length * 100, "%")

print(train_set[train_set[:, 4].argsort()])
