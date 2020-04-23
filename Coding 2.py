import numpy as np 
from openpyxl import Workbook
from openpyxl import load_workbook
import numpy as np
import matplotlib . pyplot as plt

wb  = load_workbook(filename = '9.2_recherche_developpement_TIC_20200225.xlsx')
mysheet = wb['9.2.2.7']
print(mysheet['E6'].value) 
i = 6 
x = np.arange(2006,2019,1)
yh = []
yf = []
while i <= 54 : 
    yh.append(mysheet[f'C{i}'].value)
    yf.append(mysheet[f'D{i}'].value)
    i+=4

width = 0.35
p1 = plt.bar(x-width/2, yh, width, color = 'black')
p2 = plt.bar(x+width/2, yf, width)
plt.ylabel('%')
plt.xlabel('Année')
plt.title('Part des individus (16-74 ans) ayant \n commandé des biens et services sur internet \n au cours des trois derniers mois, par sexe : 2006-2018', multialignment='center')
plt.legend((p1[0], p2[0]), ('Hommes', 'Femmes'))

plt.show()