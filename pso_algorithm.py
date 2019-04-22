import random
import numpy as np
from test_functions import sphere_model as cost_function

# Parameters
population = 100                # Number of individuals in generation
degree = 5                      # Degree of space we work on
num_of_generations = 1000       # inertia
A = 1                           # cognitive parameter
B1 = 1                          # social parameter
B2 = 1


# Individual class - Have to fix this
class Individual():

    def __init__(self, _position, _velocity, _self_best, _global_best):

        self.velocity = _velocity
        self.global_best = _global_best
        self.self_best = _self_best
        self.position = _position
        self.evaluation = cost_function(self.position)

    def __str__(self):

        return "Evaluation: " + str(self.evaluation)

    def set_global_best(self, gb):

        self.global_best = gb

    def set_self_best(self, sb):

        self.self_best = sb

    def set_self_position(self,pos):

        self.position = pos
        self.evaluation = cost_function(self.position)

    def set_velocity(self, vel):

        self.velocity = vel


def pso_ga():

    generation = init_solutions()
    best = []
    print('\nPSO algorithm:')

    for i in range(num_of_generations):

        generation = iterative_process(generation)
        generation = update_gb(generation)
        best_value = cost_function(generation[0].global_best)

        print(' Generation:' + str(i+1) + '\t Best value:' + str(best_value))

        best.append(best_value)

        if best_value < pow(10,-5):
            print('Limit reached')
            break

    return best


def init_solutions():

    generation = []
    for _ in range(population):

        position = np.array([[random.uniform(-100, 100)] for _ in range(degree)])
        velocity = np.array([[random.uniform(-1, 1)] for _ in range(degree)])
        self_best = position
        global_best = np.array([[np.infty] for _ in range(degree)])
        generation.append(Individual(position, velocity, self_best, global_best))

    generation = update_gb(generation)
    return generation


def update_gb(generation):

    current_best_eval = cost_function(generation[0].global_best)
    my_best = np.array([[np.infty] for _ in range(degree)])
    best_eval = np.infty

    for p in generation:

        if p.evaluation < best_eval:

            my_best = p.position
            best_eval = p.evaluation

    if best_eval < current_best_eval:

        for p in generation:

            p.set_global_best(my_best)

    return generation


def iterative_process(generation):

    for p in generation:

        r1 = random.random()
        r2 = random.random()

        term1 = A * p.velocity
        term2 = B1 * r1 * (p.self_best - p.position)
        term3 = B2 * r2 * (p.global_best - p.position)

        p.set_velocity(term1 + term2 + term3)
        p.set_self_position(p.position + p.velocity)

        if p.evaluation < cost_function(p.self_best):

            p.set_self_best(p.position)

    return generation



