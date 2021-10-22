import matplotlib.pyplot as plt
import numpy as np

numberofpoints = 100
x = np.random.randint(0, 500, numberofpoints)
y = x + 10 * np.random.randn(numberofpoints)
colors = np.random.randint(0, 10, numberofpoints)
sizes = np.random.randint(0, 200, numberofpoints)
plt.title("Wáőőw de hasznos ezz")
plt.scatter(x, y, s = sizes, c =colors)
plt.show()



