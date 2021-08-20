import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 100, size=(1000,))
y = np.random.randint(1, 100, size=(1000,))

x1 = np.random.randint(1, 100, size=(1000,))
y1 = np.random.randint(1, 100, size=(1000,))

plt.scatter(x, y, c="r", alpha=0.5, s=20, marker="+")
plt.scatter(x1, y1, c="b", alpha=0.5, s=20, marker="p")
plt.show()
