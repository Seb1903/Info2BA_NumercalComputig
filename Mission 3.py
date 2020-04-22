import scipy
import numpy as np

prix = np.array([
[1, 1.5, 3, 6],
[0.75,1.25, 4.3, 5.5],
[1.3, 1.6,2.5,7.5]
])  #chaque ligne correspond aux prix dans un magasin, une colonne pour un objet

i = 1
a = np.array([prix[i]])
b = np.array([50])
print(a)
x= np.linalg.solve(a,b)
print(type(a))
#print(x)
