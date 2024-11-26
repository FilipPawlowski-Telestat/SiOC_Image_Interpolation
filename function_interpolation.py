import sklearn.metrics

import functions as func
import kernel
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#Generowanie tablic wartości x + określenie długości nowego wektora
original_array = np.linspace(-np.pi,np.pi,100)
new_array = np.linspace(-np.pi,np.pi,500)

#przypisanie wartości y w zależności od wybranej funkcji
values = func.f1(original_array)

#interpolacja funkcji przez konwolucję
interpoled_valuesh1 = kernel.h1(original_array,new_array,values)
interpoled_valuesh2 = kernel.h2(original_array,new_array,values)
interpoled_valuesh3 = kernel.h3(original_array,new_array,values)

#obliczanie MSE na podstawie zinterpolowanej funkcji
print("h1: ",sklearn.metrics.mean_squared_error(func.f1(new_array),interpoled_valuesh1))
print("h2: ",sklearn.metrics.mean_squared_error(func.f1(new_array),interpoled_valuesh2))
print("h3: ",sklearn.metrics.mean_squared_error(func.f1(new_array),interpoled_valuesh3))


#utworzenie wykresu
plt.plot(original_array,func.f1(original_array), label='Original function')
plt.plot(original_array,func.f1(original_array), '.', label='Measurements')
plt.plot(new_array,kernel.h1(original_array,new_array,values),linewidth=0.7,label='Sample hold')
plt.plot(new_array,kernel.h2(original_array,new_array,values),linewidth=0.7, label='Nearest neighbour')
plt.plot(new_array,kernel.h3(original_array,new_array,values),linewidth=0.7,label='Linear')

plt.legend()

plt.show()

