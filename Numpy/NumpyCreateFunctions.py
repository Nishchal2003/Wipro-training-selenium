import numpy as np

a = np.zeros(5)
print(a)

a = np.ones(5)
print(a)

a_2D = np.ones((4,5))
print(a_2D)

a = np.arange(10)
print(a)

a = np.arange(1,10,2)
print(a)

a = np.linspace(0,10,num=5,endpoint=False)
print(a)

a = np.random.rand(5)
print(a)
a = np.random.rand(2,3)
print(a)

a = np.random.rand(2,3,4)
print(a)

a = np.empty((2,3))
print("\n",a)