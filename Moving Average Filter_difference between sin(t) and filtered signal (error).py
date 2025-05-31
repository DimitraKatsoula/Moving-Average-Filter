# PYTHON CODE - Moving Average Filter
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi, np.pi, 100)
np.random.seed(0)
x = np.sin(t) + 0.25 * np.random.rand(len(t))

window_size = 5
b = np.ones(window_size) / window_size
y = np.convolve(x, b, mode='same')
# Filter 1 continue:
# Same as above, with an additional plot showing the difference
# between sin(t) and filtered signal (error).
np.random.seed(0)
t = np.linspace(-np.pi, np.pi, 100)
x = np.sin(t) + 0.25 * np.random.rand(len(t))
y = np.convolve(x, b, mode='same')
plt.plot(t, x, label='Input Data with noise=x')
plt.plot(t, y, label='Filtered Data without noise=y')
plt.plot(t, np.sin(t) - y, label='signal with no noise-filtered=~0')
plt.legend()
plt.show()




