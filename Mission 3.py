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
def np_multiply(a, b):      #produit scalaire
    np.dot(a,b)         #essayer de créer des objets matrices pour comparer avec la méthode dot

def result1(x) : 
    REPEATS = 1000
    a = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]   #génère matrices carrées de pus en plus grandes, a et b sont toutes les 2 des matrices 
    b = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]
    # Measure execution time of py_multiply
    t = timeit.Timer(f'py_multiply({a}, {b})', '''from __main__ import py_multiply''')   #j'ai du modifier la fonction car j'avais des unexpected indent sinon
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 


def result2(x) : 
    REPEATS = 1000
    # Measure execution time of np_multiply
    a = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]
    b = [[random.randint(1,10) for x in range(int(x))] for y in range(int(x))]
    t = timeit.Timer(f'np_multiply({a}, {b})', '''from __main__ import np_multiply''')
    result = t.timeit(REPEATS) / REPEATS * 1000
    print(result, 'ms')
    return result 

#def plot() : 
x = np.arange(1,20,1, dtype = int)
y1= []
for i in x :      #permet de prendre chaque valeur séparément, sinon y essayait l'array tout entier dans result1
    print(i) 
    y1.append(result1(i))            #permet de retenir chaque résultat sinon ne plottait que le premier 


y2 = []
for i in x :      #permet de prendre chaque valeur séparément, sinon y essayait l'array tout entier dans result1
    print(i) 
    y2.append(result2(i))  


plt.plot(x, y2, label ='Array')
plt.plot(x, y1,color = 'red',label ='Explicit')

plt.show ()

#plot()