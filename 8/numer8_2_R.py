# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:13:50 2018

@author: Yuki-F
"""

#Lagrange interpolation
import numpy as np
import matplotlib.pyplot as plt

n = 11
x = [-4.91, -3.91, -2.93, -1.90, -0.95,
     0.09, 1.07, 2.07, 3.09, 4.10, 5.06]
y = [-34.6, 12.2, 39.4, 41.1, 25.5,
     10.4, 4.5, -7.9, -2.8, 19.9, 64.8]


#Determine coefficients
p = np.polyfit(x, y, n-1)
xx = np.linspace(-5.5, 5.5, 200)
yy = np.polyval(p, xx)

#Answer to (b)
ans = np.polyval(p, np.arange(-4.5, 4.5, 1.5))
print(ans)

#plot data
plt.plot(x, y, 'ro') #Sampled data
plt.xlabel('x')
plt.ylabel('y')
plt.hold(True)
plt.plot(xx, yy, 'm') #Polynomial interpolation
