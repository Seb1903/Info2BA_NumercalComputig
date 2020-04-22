import scipy
import numpy as np
import matplotlib.pyplot as plt 
import timeit

a = [
    [1,0],
    [0,1]
    ] 
b = [
    [3,1],
    [4,5]
    ]
# Explicit multiplication by manipulating Python lists with loops
def py_multiply(a, b):
    res = [[0 for x in range(len(a))] for y in range(len(b))]
    for i in range(len(a)): 
        for j in range(len(b[0])): 
            for k in range(len(b)): 
                res[i][j] += a[i][k] * b[k][j] # résultat

# Direct multiplication with the ndarray or matrix object
def np_multiply(a, b):
    np.dot(a,b)         #essayer de créer des objets matrices pour comparer avec la méthode dot


REPEATS = 1000

# Measure execution time of py_multiply
t = timeit.Timer('py_multiply(p, p)', '''from __main__ import py_multiply
p = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]''')
result = t.timeit(REPEATS) / REPEATS * 1000
print(result, 'ms')

# Measure execution time of np_multiply
t = timeit.Timer('np_multiply(p, p)', '''import numpy as np
from __main__ import np_multiply
p = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])''')
result = t.timeit(REPEATS) / REPEATS * 1000
print(result, 'ms')