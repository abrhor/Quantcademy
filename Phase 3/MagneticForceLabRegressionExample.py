import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.optimize import curve_fit

sf40 = 1. * (10. ** -2) # various wire lengths (supplements)
sf37 = 2. * (10 ** -2)
sf38 = 4. * (10 ** -2)
sf39 = 3. * (10 ** -2)

m = 165.1 * (10.**-3) # mass of magnets
mg = m * 9.8
voltage = 6.

l = sf39 # Constant length, altering current (via rheostat), output is mass
current = np.array([2.8, 1.1, 2., .5])
newmasses1 = np.array([164.3, 164.7, 164.5, 164.8])
sns.regplot(current, newmasses1)
plt.xlabel('Current (Amps)')
plt.ylabel('Mass (Grams)')
plt.title('Current in Wire vs. Measure Mass of Magnets (Length = .03 Meters)')
plt.show()

current2 = 1. # Constant current, altering length, output is mass
lengths2 = np.array([sf39, sf40, sf38])
masses2 = np.array([164.7, 164.8, 164.6])
ms = np.array([m * (10**3) for i in lengths2])

regplot(lengths2, masses2, label='Data')
regplot(lengths2, ms, marker='.', color='r',  label='Original mass')
plt.xlabel('Wire Length (Meters)')
plt.ylabel('Measured Mass (Grams)')
plt.legend(loc='upper right')
plt.title('Length of Supplementary Wire vs. Measured Mass of Magnets')

ms = np.array([m * (10**3) for i in range(100)])
length  = sf39 # Constant length, altering B (by changing the number of magnets), output is mass
b = np.array([6., 5., 4.) 
masses3 = np.array([164.7, 152., 139.2])
regplot(b, masses3, label='Data')
regplot(np.arange(100), ms, marker='.', color='r',  label='Original mass')
plt.xlabel('Number of Magnets')
plt.ylabel('Measured Mass (Grams)')
plt.legend(loc='upper right')
plt.title('Number of Magnets vs. Measured Mass of Magnets')


def lin(x, m, b):
  return m * x + b
  
ws, cov = curve_fit()
