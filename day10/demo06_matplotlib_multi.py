import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13)
y1 = np.random.randint(1, 100, size=(12,))
y2 = np.random.randint(1, 100, size=(12,))
y3 = np.random.randint(1, 100, size=(12,))
y4 = np.random.randint(1, 100, size=(12,))

plt.plot(x, y1, c="r", label="a")
plt.plot(x, y2, c="b", label="b")
plt.plot(x, y3, c="g", label="c")
plt.plot(x, y4, c="r", label="d")
plt.show()
