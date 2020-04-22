import scipy
import numpy as np
import matplotlib.pyplot as plt 
import timeit
import random


'''a = [[random.randint(1,10) for x in range(int(3))] for y in range(int(3))]
b = [[random.randint(1,10) for x in range(int(3))] for y in range(int(3))]'''

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

def result1(x) : 
    REPEATS = 1000
    a = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]
    b = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]
    # Measure execution time of py_multiply
    t = timeit.Timer(f'py_multiply({a}, {b})', '''from __main__ import py_multiply''')
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 


def result2() : 
    REPEATS = 1000
    # Measure execution time of np_multiply
    t = timeit.Timer(f'np_multiply({a}, {b})', '''import numpy as np
    from __main__ import np_multiply''')
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 

#def plot() : 
x = np.linspace(0,100, 5)
y = result1(x)

plt.plot (x, y)
plt.show ()

#plot()