import pygad
import numpy
import time

S = [["zegar", 100, 7],
     ["obraz-pejzaż", 300, 7],
     ["obraz-portret", 200, 6],
     ["radio", 40, 2],
     ["laptop", 500, 5],
     ["lampka nocna", 70, 6],
     ["srebrne sztućce", 100, 1],
     ["porcelana", 250, 3],
     ["figura z brązu", 300, 10],
     ["skórzana torebka", 280, 3],
     ["odkurzacz", 300, 15]]

# print(S)

# definiujemy parametry chromosomu
# geny to liczby: 0 lub 1
gene_space = [0, 1]


# definiujemy funkcję fitness
def fitness_func(ga_instance, solution, solution_idx):
    wartosc = []
    waga = []
    for key in S:
        wartosc.append(key[1])
        waga.append(key[2])
    sum1 = numpy.sum(solution * wartosc)
    sum2 = numpy.sum(solution * waga)
    # print(sum1, sum2)
    if sum2 > 25:
        fitness = 0
    else:
        fitness = numpy.abs(sum1)
    # lub: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
    return fitness


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

# ile wylaniamy rodzicow do "rozmnazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w ilu punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

start = time.time()
# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_1600"])

# uruchomienie algorytmu
ga_instance.run()
end = time.time()
# średni czas 0,01170060634613030
print("Czas trwania: ", end - start)
# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Number of generations passed is {ga_instance.generations_completed}")
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
lista = []
solution_list = solution.tolist()
print(solution_list)
for i in range(0, len(solution_list)):
    if solution_list[i] == 1:
        lista.append(S[i])
print(f"Best to take is: {lista}")

# tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
wartosc = []
waga = []
for key in S:
    wartosc.append(key[1])
    waga.append(key[2])
prediction = numpy.sum(wartosc * solution)
prediction2 = numpy.sum(waga * solution)
print(f"Predicted output based on the best solution : {prediction}\nwith weight: {prediction2}")

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
