import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return [0.5 * xi for xi in x]
def f2(x):
    return 0.5 * x 
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [1.2, 2.5, 3.8, 4.7, 6.2, 7.3, 6.1, 4.6, 4.3, 3.8]

#dumm geht einfach nicth
for i in range(len(x_values)):
    if np.round(f2(x_values[i]),1) in y_values:
        print("hi",y_values[i],f2(x_values[i]),x_values[i])
    else:
        print("Affen",y_values[i],f2(x_values[i]),x_values[i])
plt.plot(x_values,y_values)
plt.plot(x_values,f(x_values))
plt.show()
