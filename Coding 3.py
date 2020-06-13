import numpy as np 
from openpyxl import Workbook
from openpyxl import load_workbook
import numpy as np
import matplotlib . pyplot as plt

wb  = load_workbook(filename = 'quiz-gs.xls.xlsx')
mysheet = wb['Sheet']
i = 2 
âge = []
superficie = []
while i <= 1556 :
    try : 
        if mysheet[f'L{i}'].value <= 500 : 
            âge.append(mysheet[f'D{i}'].value)
            superficie.append(mysheet[f'L{i}'].value)
    except TypeError : 
        pass
    i+=1

width = 0.35

plt.ylabel("Superficie en m^2")
plt.xlabel('âge')
plt.title("Superficie d'habitation de l'âge", multialignment='center')
marker_size=5
plt.scatter(âge, superficie,marker_size)
#np.polyfit(âge, superficie)
plt.show()