import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from keras.models import Sequential
from keras.layers import Dense

# Wczytaj dane
df = pd.read_csv('diabetes.csv')

# Wybierz kolumny cech i docelową
target_column = ['class']
predictors = list(set(list(df.columns)) - set(target_column))

# Normalizuj dane
df[predictors] = df[predictors] / df[predictors].max()

# Mapowanie klas na liczby (0 i 1)
class_mapping = {'tested_negative': 0, 'tested_positive': 1}
df['class'] = df['class'].map(class_mapping)

# Przygotuj dane wejściowe i wyjściowe
X = df[predictors].values
y = df[target_column].values

# Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)

# Zdefiniuj model
model = Sequential()
model.add(Dense(6, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Skompiluj model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Wytrenuj model na zbiorze treningowym, zapisując historię
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=500, batch_size=10, verbose=0)

# Ewaluacja na zbiorze testowym
y_pred = np.argmax(model.predict(X_test), axis=1).ravel()
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Dokładność (Accuracy): {:.2f}%".format(accuracy * 100))
print("\nMacierz błędu:\n", conf_matrix)

# Narysuj krzywą błędu
train_loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(train_loss) + 1)

plt.plot(epochs, train_loss, 'g', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
