import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.title("Histogram")
plt.xlabel("Random Data")
plt.ylabel("Frequency")
plt.hist(x,10)
plt.show()