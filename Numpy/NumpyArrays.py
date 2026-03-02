import numpy as np
a = np.array([1,2,3])
print(a)

a = np.array([[1,2],[2,4]])
print(a)

a = np.array([[1,2],[2,4],[3,4]])
print(a)

a= np.array([1,2,3],dtype=complex)
print(a)

a= np.array([1,2,3],dtype=float)
print(a)

a= np.array([1,2,3],dtype=int)
print(a)

identity_matrix = np.eye((4))
print("\n",identity_matrix)

Matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Original Matrix\n",Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements",Diagonal_elements)