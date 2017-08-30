import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)

ws = np.array([14., 30.])
w = 14.
b = 30.
n = 1000.
x = np.array([float(i) for i in range(1000)])

b_h = w_h = 15.

def linear(a, x, b):    
  return a * x + b
y = linear(14., x, b)
y_h = linear(w_h, x, b_h)
def mse(actual, expected, n):    
  return 1. / n * np.nansum((expected-actual)**2)  
c = np.array([mse(y, y_h, n)])
w_t = np.array([w_h])
b_t = np.array([b_h])
for i in range(1000):  
  w_h += (y_h-y).T.dot(x) * -2. * .00001 / n  
  b_h += -np.sum(y_h-y) * 2. * .00001 / n  
  w_t = np.append(w_t, w_h)  b_t = np.append(b_t, b_h)  
  c = np.append(c, mse(y, linear(w_h, x, b_h), n))
  
plt.plot(w_t[1:], c[1:])
plt.title("Trajectory of Weight")
plt.xlabel("Cost")
plt.ylabel("Value of Weight")
print(w_t[0], b_t[0])
