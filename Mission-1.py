import scipy
import numpy as np 

data3 = np.array([[['h','e','l','l','o'] , [2]] , [['w','o','r','l','d'] , [4]]])

helloconq = ""
worldconq = ""
for i in range(5): 
   helloconq += data3[0,0][i]
   worldconq += data3[1,0][i]
concatenation = np.array([[helloconq],[worldconq]])
print(concatenation)

concatenation2 = concatenation.reshape(1,2)
print(concatenation2)