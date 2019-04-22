import de_algorithm
import tkinter
import matplotlib.pyplot as plt
import pso_algorithm

de_values = de_algorithm.de_ga()
pso_values = pso_algorithm.pso_ga()

plt.figure()
plt.plot(range(len(de_values)), de_values, label = 'DE algorithm')
plt.plot(range(len(pso_values)), pso_values, label = 'PSO algorithm')
plt.legend()
plt.title('Genetic algoriths')
plt.show()

