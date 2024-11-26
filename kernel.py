import numpy as np


#funkcje jądrowe z wbudowaną interpolacją

#sample and hold
def h1(original_array, new_array, values):
    step = original_array[2] - original_array[1]
    interpoled_array = np.zeros(len(new_array))

    for i in range(len(original_array)):
        for j in range(len(new_array)):
            if original_array[i]<=new_array[j]<original_array[i]+step:
                interpoled_array[j] = values[i]
    return interpoled_array

#nearest neighbour
def h2(original_array, new_array, values):
    step = original_array[2] - original_array[1]
    interpoled_array = np.zeros(len(new_array))

    for i in range(len(original_array)):
        for j in range(len(new_array)):
            if original_array[i]-step/2<=new_array[j]<original_array[i]+step/2:
                interpoled_array[j] = values[i]
    return interpoled_array


#hut
def h3(original_array, new_array, values):
    step = np.abs(original_array[2] - original_array[1])
    interpoled_array = np.zeros(len(new_array))
    temp_array=new_array.copy()

    for i in range(len(original_array)):
        for j in range(len(new_array)):
            if original_array[i]-step<=new_array[j]<original_array[i]+step:
                temp_array[j]=1-np.abs(new_array[j]-original_array[i])
                interpoled_array[j] = temp_array[j]*values[i]
    return interpoled_array

