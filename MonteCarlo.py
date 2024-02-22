import numpy as np
import matplotlib.pyplot as plt

sims = 10000000

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

duração = A + B

plt.figure(figsize=(11, 5.5))
plt.hist(duração, density = True)
plt.axvline(8, color = "r")
plt.show()