#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:20:33 2022

@author: neutrino
"""

import matplotlib.pyplot as plt
import sympy as sy
import numpy as np



# x axis values
x = [
0,
0.32,
0.94,
1.76,
2.38,
3.06,
3.84,
4.3,
4.8,
5.36,
5.9,
6.2,
6.46,
6.08,
5.48,
4.96,
4.4,
3.74,
3.14,
2.28,
1.7,
1.02,
0.4,
0]
# corresponding y axis values
y = [
+0,
+0.54,
+1.22,
+1.56,
+1.64,
+1.56,
+1.4,
+1.26,
+1.08,
+0.76,
+0.38,
+0.2,
+0,
-0.6,
-0.98,
-1.28,
-1.46,
-1.62,
-1.68,
-1.68,
-1.6,
-1.26,
-0.74,
0]

# plotting the points
if len(x)==len(y):
    plt.plot(x,y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Leaf')
    plt.show()
else:
    print("The number of x and y coordinates do not match")
    
coeffs = [-0.0000750865,0.00265006,-0.0406888,0.356286,-1.95885,7.01039,-16.3582,24.1663,-20.9625,8.59085,0.443098,0]
list_polynomial = np.poly1d(coeffs)
integration = np.polyint(list_polynomial)
print("The polynomial: ")
print(list_polynomial)
print("\n\nThe integrated polynomial:")
print(integration)
intg = (integration(max(x)) - integration(0))
print(f"\nIntegral of the polynomial: {intg}")
print(f"Area: {intg*2} units")