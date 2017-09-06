import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model

xs = np.arange(100)
signal = np.linspace(1, 200, 100) # m = 2x
noise = np.random.normal(60, 15, 100) # mean of 60, so skewed right, and sigma of 15.
ys = signal + noise
plt.plot(xs, ys)

model = sklearn.linear_model.LinearRegression()
model.fit(xs, ys)
