import math
import pygad
import time

S = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
     ['*', 'S', '.', '.', '*', '.', '.', '.', '*', '.', '.', '*'],
     ['*', '*', '*', '.', '.', '.', '*', '.', '*', '*', '.', '*'],
     ['*', '.', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*'],
     ['*', '.', '*', '.', '*', '*', '.', '.', '*', '*', '.', '*'],
     ['*', '.', '.', '*', '*', '.', '.', '.', '*', '.', '.', '*'],
     ['*', '.', '.', '.', '.', '.', '*', '.', '.', '.', '*', '*'],
     ['*', '.', '*', '.', '.', '*', '*', '.', '*', '.', '.', '*'],
     ['*', '.', '*', '*', '*', '.', '.', '.', '*', '*', '.', '*'],
     ['*', '.', '*', '.', '*', '*', '.', '*', '.', '*', '.', '*'],
     ['*', '.', '*', '.', '.', '.', '.', '.', '.', '.', 'E', '*'],
     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
     ]

# 4 - lewo, 8 - góra, 6 - prawo, 2 - dół
gene_space = [4, 8, 6, 2]

# współrzędne startu 
start = [(i, s.index('S'))
         for i, s in enumerate(S)
         if 'S' in s][0]

# współrzędne wyjścia
exit = [(i, s.index('E'))
        for i, s in enumerate(S)
        if 'E' in s][0]


# print(start, exit)
# print(S[2][2])
# print(len(S))

def fitness_func(ga_instance, solution, solution_idx):
    y, x = start
    for step in solution:
        if step == 4:
            if S[y][x - 1] != "*" and -1 < x - 1 < len(S[0])-1:
                x = x - 1
        elif step == 8:
            if S[y - 1][x] != "*" and -1 < y - 1 < len(S)-1:
                y = y - 1
        elif step == 6:
            if S[y][x + 1] != "*" and -1 < x + 1 < len(S[0])-1:
                x = x + 1
        elif step == 2:
            if S[y + 1][x] != "*" and -1 < y + 1 < len(S)-1:
                y = y + 1

    fitness = -((exit[0] - y) ** 2 + (exit[1] - x) ** 2) ** 0.5
    return fitness


fitness_function = fitness_func

sol_per_pop = 10
num_genes = 30

num_parents_mating = 5
num_generations = 500
keep_parents = 2

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 4

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
                       stop_criteria=["reach_0"])
startTime = time.time()
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
endTime = time.time()
# średni czas działania programu przy fitness = 0 wynosi 0,0824328184127805
print("Czas trwania: ", endTime - startTime)
ga_instance.plot_fitness()
