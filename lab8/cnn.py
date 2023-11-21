import numpy as np
from matplotlib import pyplot as plt

# tworzymy tablice o wymiarach 128x128x3 (3 kanaly to RGB)
# uzupelnioną zerami = kolor czarny
data = np.zeros((128, 128, 1), dtype=np.uint8)

print(data)


# chcemy zeby obrazek byl czarnobialy,
# wiec wszystkie trzy kanaly rgb uzupelniamy tymi samymi liczbami
# napiszmy do tego funkcje
def draw(img, x, y, color):
    img[x, y] = color


# zamalowanie 4 pikseli w lewym górnym rogu
draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)

# rysowanie kilku figur na obrazku
for i in range(128):
    for j in range(128):
        if (i - 64) ** 2 + (j - 64) ** 2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i - 15) ** 2 + (j - 110) ** 2 < 25:
            draw(data, i, j, 150)
        elif (i - 15) ** 2 + (j - 110) ** 2 == 25 or (i - 15) ** 2 + (j - 110) ** 2 == 26:
            draw(data, i, j, 255)

filtr = np.array([[1, 0, -1],
                  [1, 0, -1],
                  [1, 0, -1]])

print(filtr[1, 0])

result_b = np.zeros((126, 126, 1), dtype=np.uint8)
for i in range(128-2):
    for j in range(128-2):
        result_b[i, j] = (data[i, j] * filtr[0, 0] + data[i, j + 1] * filtr[0, 1] + data[i, j + 2] * filtr[0, 2] +
                          data[i + 1, j] * filtr[1, 0] + data[i + 1, j + 1] * filtr[1, 1] + data[i + 1, j + 2] * filtr[
                              1, 2] +
                          data[i + 2, j] * filtr[2, 0] + data[i + 2, j + 1] * filtr[2, 1] + data[i + 2, j + 2] * filtr[
                              2, 2])

print(result_b)

result_c = np.zeros((126, 126, 1), dtype=np.uint8)
for i in range(128-1, 2):
    for j in range(128-1, 2):
        result_c[i, j] = (data[i, j] * filtr[0, 0] + data[i, j + 1] * filtr[0, 1] + data[i, j + 2] * filtr[0, 2] +
                          data[i + 1, j] * filtr[1, 0] + data[i + 1, j + 1] * filtr[1, 1] + data[i + 1, j + 2] * filtr[
                              1, 2] +
                          data[i + 2, j] * filtr[2, 0] + data[i + 2, j + 1] * filtr[2, 1] + data[i + 2, j + 2] * filtr[
                              2, 2])

# konwersja macierzy na obrazek i wyświetlenie
# plt.imshow(data, interpolation='none', cmap='gray')
# plt.show()
# plt.imshow(result_b, cmap='gray')
# plt.show()
plt.imshow(result_c, cmap='gray')
plt.show()
