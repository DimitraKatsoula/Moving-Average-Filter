# PYTHON CODE - Moving Average Filter
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi, np.pi, 100)
np.random.seed(0)
x = np.sin(t) + 0.25 * np.random.rand(len(t))

window_size = 5
b = np.ones(window_size) / window_size
y = np.convolve(x, b, mode='same')

plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Input Data with Noise: x')
plt.plot(t, y, label='Filtered Data: y', linewidth=2)
plt.title('Moving Average Filter (Window Size = 5)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


