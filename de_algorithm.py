import random
import numpy as np
from test_functions import sphere_model as cost_function

# Parameters
population = 100              # Number of individuals in generation
degree = 5                    # Degree of space we work on
num_of_generations = 1000     # number of generations
q = 0.5                      # parameter of da
H = 0.2                       # for probability


# Individual class - Have to fix this
class Individual():

    def __init__(self, vector):

        self.vector = vector
        self.evaluation = cost_function(self.vector)

    def __str__(self):

        return "Evaluation: " + str(self.evaluation)

    def __add__(self, other):

        return Individual(self.vector + other.vector)

    def __sub__(self, other):

        return Individual(self.vector - other.vector)

    def __mul__(self, other):

        if isinstance(other, self.__class__):
            print(' You cannot multiply that')
            return
        elif isinstance(other, float):

            return Individual(other * self.vector)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))


def de_ga():

    generation = init_solutions(population, degree)
    best = []
    print('\nDE algorithm:')
    for i in range(num_of_generations):

        secondary = mutation(generation)
        offspring = crossover(generation, secondary)
        generation = selection(generation, offspring)

        best_value = give_best(generation)

        print(' Generation:' + str(i+1) + '\t Best value:' + str(best_value))

        best.append(best_value)

        if best_value < pow(10,-5):
            print('Limit reached')
            break

    return best


def init_solutions(_population, _degree):

    generation = []

    for _ in range(_population):

        vector = np.array([[random.uniform(-100, 100)] for _ in range(degree)])
        generation.append(Individual(vector))

    return generation


def mutation(generation):

    secondary = []

    for _ in range(population):

        r1 = random.randrange(0, population - 1)
        r2 = random.randrange(0, population - 1)
        r3 = random.randrange(0, population - 1)

        secondary.append(generation[r1] + ((generation[r2] - generation[r3]) * q))

    return secondary


def crossover(p, u):

    l = random.randrange(0, population - 1)
    offspring = []

    for i in range(len(p)):

        if i == l:
            offspring.append(u[i])
        else:
            h = random.random()
            offspring.append(u[i]) if h <= H else offspring.append(p[i])

    return offspring


def selection(p,v):

    next_generation = []

    for i in range(len(p)):

        next_generation.append(p[i]) if p[i].evaluation < v[i].evaluation else next_generation.append(v[i])

    return next_generation


# to be fixed
def give_best(generation):

    return min([member.evaluation for member in generation])