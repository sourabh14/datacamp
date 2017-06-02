# Data science packages
import numpy as np

# numpy arrays allows easy and fast 
# operations over entire array elements
arr = np.array([1,2,3,4])
print(arr)

double_arr = arr + arr
print("double of array: ")
print(double_arr)

height = [1.73, 1.68, 1.71]
weight = [65.4, 59.2, 63.6]

np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2

print("bmi: ")
print(bmi)

bmi2 = bmi > 21
print("boolean array for bmi greater than 21")
print(bmi2)

