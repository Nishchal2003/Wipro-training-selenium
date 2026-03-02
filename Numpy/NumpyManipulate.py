import numpy as np
from numpy.ma.core import indices
from numpy.ma.extras import hstack

a = np.arange(1,7)
print("Original array:\n",a)

reshaped = a.reshape(2,3)
print(reshaped)

# Flat - Return 1D iterator over the array
arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)
#Flatten - Returns a copy of the array collapsed into one direction.
arr = np.array([[1,2],[3,4]])
print(arr)
att_arr = arr.flatten()
print(att_arr)

# Reavel method -  Returns a flattened array
arr = np.array([[1,2],[3,4]])
for x in arr.ravel():
    print(x)

arr = np.array([[1,2],[3,4]])
padded = np.pad(arr,2,mode='constant')
print(padded)

# Transopose
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transponse = arr.T
print(transponse)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

#2.ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transponse = arr.T

#Concatinate
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,20,30],[40,50,60]])

print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

print(hstack((a,b)))# same as axis = 1
print(np.vstack((a,b)))#same as axis = 0

# Splitting Arrays
# Split arrays into multiple sub-arrays based on axis.
arr = np.array([1,2,3,4,5,6])
result = np.split(arr,3)
print(result)

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr2,2))
arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(arr2,2))
print(np.array_split(arr,3))

arr = np.array([1,2,3,4,5,6])
new_arr = np.resize(arr,(2,3))
print("\n",new_arr)

arr = np.array([1,2,3])
new_arr = np.append(arr,[4,5])
print("\n",new_arr)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

print("\n",np.append(a, b, axis=0))
#Delete specified elements
new_arr = np.delete(arr,2)
print("\n",new_arr)
#Unique
arr = np.array([1,2,3,3,4,5,5])
print(np.unique(arr))

#Different Repeats foreach element
arr = np.array([10,20,30])
print("\n",np.repeat(arr,[1,2,3]))

# Repeate in 2D array
arr2 = np.array([[1,2],[3,4]])
print(np.repeat(arr2,2,axis=0))

#Tile() The input array that will repeat
my_arr = np.array([1,2,3])
tiled_array = np.tile(my_arr,2)
print("Original array:",my_arr)
print("Tiled array:",tiled_array)

# Rearanging Elements
# flip() - Reverses the order of the elements along a given axis.
# If axis  = None -> Reverse entire flattened array
# If axis = 0 -> Reverse rows
# If axis = 1-> Reverse columns

arr = np.array([10,20,30])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],[3,4]])
print(np.fliplr(arr2))
print(np.flipud(arr2))

arr2 = np.array([[1,2],[3,4]])
np.roll(arr2,2,axis=None)

# Sorting and Searching
arr = np.array([10,20,7,5])
indices = np.argsort(arr)
print("\n",indices)

# lexsort() - Used for sorting with multiple columns(like sorting by last name, then first name)
a = np.array([1,1,0,0])
b = np.array([1,0,1,0])
result = np.lexsort((a,b))
print(result)

