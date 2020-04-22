import scipy
import numpy as np 

data = np.array([['h','e','l','l','o','w','o','r','l','d'],[1,2,2,3,4,5,6,7,8,9]]),

helloconq = ""
worldconq = ""
for i in range(5): 
   helloconq += data[0][0][i]
   worldconq += data[0][0][5+i]
print(data[0][0])
conqmatrice = np.array([[helloconq],[worldconq]])
print(conqmatrice)







#  shape = (1,10)
# donnee = np.ndarray(shape)

#  a= 0
#  b=0
#  for i in range(10) : 
#      donnee[a,b] = i
#      b += 1
#  print(donnee)
