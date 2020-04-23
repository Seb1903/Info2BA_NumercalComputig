import scipy
import numpy as np
import matplotlib.pyplot as plt 
import timeit
import random

def py_min(a) : 
    min = 9999999 
    for i in a : 
        for elem in i : 
            if elem < min : 
                min = elem 
    return min 

def np_min(a) :
    return np.min(a)

def time_py(i) : 
    a = [[random.randint(1,10) for x in range(int(i))] for y in range(int(i))]
    REPEATS = 1000
    t = timeit.Timer(f'py_min({a})', '''from __main__ import py_min''')   #j'ai du modifier la fonction car j'avais des unexpected indent sinon
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 
def time_np(i) : 
    a = [[random.randint(1,10) for x in range(int(i))] for y in range(int(i))]
    REPEATS = 1000 
    t = timeit.Timer(f'np_min({a})', '''from __main__ import np_min''')
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 


x = np.arange(1,20,1, dtype = int)
y1= []
for i in x :      
    print(i) 
    y1.append(time_py(i))            


y2 = []
for i in x :      
    print(i) 
    y2.append(time_np(i))  


plt.plot(x, y2, label ='Numpy')
plt.plot(x, y1,color = 'red',label ='Py')
plt.show()