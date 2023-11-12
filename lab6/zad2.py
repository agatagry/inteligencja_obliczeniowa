from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

iris = load_iris()
train_data, test_data, train_labels, test_labels = train_test_split(iris.data, iris.target, train_size=0.7)

# scaling the data
scaler = StandardScaler()

# we fit the train data
scaler.fit(train_data)

# scaling the train data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

print(train_data[:3])

# creating a classifier from the model:
mlp = MLPClassifier(hidden_layer_sizes=(2, ), max_iter=3000)

# let's fit the training data to our model
mlp.fit(train_data, train_labels)

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))
predictions_test1 = mlp.predict(test_data)
accuracy_test1 = accuracy_score(predictions_test1, test_labels)
print(accuracy_test1)

print(confusion_matrix(predictions_train, train_labels))
print(confusion_matrix(predictions_test1, test_labels))

print(classification_report(predictions_test1, test_labels))

mlp = MLPClassifier(hidden_layer_sizes=(3, ), max_iter=3000)

mlp.fit(train_data, train_labels)

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))
predictions_test2 = mlp.predict(test_data)
accuracy_test2 = accuracy_score(predictions_test2, test_labels)
print(accuracy_test2)

mlp = MLPClassifier(hidden_layer_sizes=(3, 2), max_iter=3000)

mlp.fit(train_data, train_labels)

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))
predictions_test3 = mlp.predict(test_data)
accuracy_test3 = accuracy_score(predictions_test3, test_labels)
print(accuracy_test3)


print("najlepszy wynik:", max(accuracy_test1, accuracy_test2, accuracy_test3))
