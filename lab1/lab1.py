# import math
import os
import random
import pandas as pd
import matplotlib
from matplotlib import pyplot


# zad1
def prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def select_primes(x):
    result = []
    for i in x:
        if prime(i):
            result.append(i)
    return result


print(prime(16))
print(select_primes([3, 6, 11, 25, 19]))

# zad2
tab1 = [3, 8, 9, 10, 12]
tab2 = [8, 7, 7, 5, 6]


# a
def sum_vector(vec1, vec2):
    result = []
    if len(vec1) == len(vec2):
        for i in range(0, len(vec1)):
            result.append(vec1[i] + vec2[i])
    return result


print(sum_vector(tab1, tab2))


def multiply_vector(vec1, vec2):
    result = []
    if len(vec1) == len(vec2):
        for i in range(0, len(vec1)):
            result.append(vec1[i] * vec2[i])
    return result


print(multiply_vector(tab1, tab2))


# b
def scalar_vector(vec1, vec2):
    return sum(multiply_vector(vec1, vec2))


print(scalar_vector(tab1, tab2))


# c
def euklidean_length(vec1, vec2):
    sum_of_sq = 0
    if len(vec1) == len(vec2):
        for i in range(0, len(vec1)):
            sum_of_sq += (vec1[i] - vec2[i]) ** 2
    return sum_of_sq ** 0.5


print(euklidean_length(tab1, tab2))

# d
vector = []
for i in range(0, 50):
    vector.append(int(random.random() * 100 + 1))
print(vector)

# e
srednia = round(sum(vector) / len(vector), 2)
suma = 0
for i in vector:
    suma += (i - srednia) ** 2

print("średnia elementów: ", srednia, "\nMinimum: ", min(vector), "\nMaksimum: ", max(vector),
      "\nOdchylenie standardowe: ", round((suma / len(vector)) ** 0.5, 2))

# f
normalizacja = []
for i in range(0, len(vector)):
    normalizacja.append(round((vector[i] - min(vector)) / (max(vector) - min(vector)), 3))

pozycja_max = vector.index(max(vector))
print(normalizacja)
print("pozycja max:", pozycja_max)
print("Wartośc na pozycji max: ", normalizacja[pozycja_max])

# g
standaryzacja = []
for i in range(0, len(vector)):
    standaryzacja.append(round((vector[i] - srednia) / (round((suma / len(vector)) ** 0.5, 2)), 3))

print(standaryzacja)
suma = 0
for i in standaryzacja:
    suma += (i - srednia) ** 2

print("srednia: ", round(sum(standaryzacja) / len(standaryzacja), 2),
      "\nodchylenie standardowe: ", round((suma / len(standaryzacja)) ** 0.5, 2))

# zad 3

# a
miasta = pd.read_csv("miasta.csv")
print(miasta)
print(miasta.values)

#b
miasta = pd.DataFrame(miasta)
miasta.loc[len(miasta)] = [2010, 460, 555, 405]
print(miasta)

#c
x = miasta['Rok'].to_numpy()
y = miasta['Gdansk'].to_numpy()
pyplot.plot(x, y, ".-r")
pyplot.title("Populacja Gdańska w latach 1900 - 2010")
pyplot.xlabel("Lata")
pyplot.ylabel("Liczba ludności [w tys.]")
pyplot.grid(True)
pyplot.show()

#d
df = pd.DataFrame(miasta)
x = miasta['Rok'].to_numpy()
pyplot.plot(x, miasta['Gdansk'].to_numpy(), ".-b", label="Gdańsk")
pyplot.plot(x, miasta['Poznan'].to_numpy(), ".-r", label="Poznań")
pyplot.plot(x, miasta['Szczecin'].to_numpy(), ".-g", label="Szczecin")
pyplot.title("Populacja miast w latach 1900 - 2010")
pyplot.xlabel("Lata")
pyplot.ylabel("Liczba ludności [w tys.]")
pyplot.legend()
pyplot.grid(True)
pyplot.show()
