# Datacamp Lists
import math

# data types in python
# int str bool float

# Lists ----------------------------------------------------------
arr = [1, 2, 3, 4, 5]
print(arr)

twodarray = [
				["abc", 1],
				["def", 2]
			]
print(twodarray)		

# slicing list
print("Array elements from index 2 to 4")	
print(arr[2:5])
print("Array elements from index 0 to 2")	
print(arr[:3])
print("first two elements")	
print(arr[:-3])
print("last 3 elements")	
print(arr[-3:])

# adding elements to list
twodarray.insert(1, list(["xyz", 3]))
print(twodarray)

# deleting elements
del(twodarray[1])
print(twodarray)

# merging two lists
arr2 = [6, 7, 8]
arr = arr2 + arr
print(arr)

# Inbuilt Functions ----------------------------------------------------------
print("max of array: " + str(max(arr)))
print("round of 1.68 to one decimal place: " + str(round(1.68,1)))
print("sorted array: " + str(sorted(arr)))
print("length of array is : " + str(len(arr)))

print("value of pi " + str(round(math.pi, 2)))