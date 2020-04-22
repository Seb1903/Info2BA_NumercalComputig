
import scipy
import numpy as np

opération = input('opération ? ')

prix = np.matrix([
[1, 1.5, 3, 6],
[0.75,1.25, 4.3, 5.5],
[1.3, 1.6,2.5,7.5],
[2, 1, 4, 8]
])  #chaque ligne correspond aux prix dans un magasin, une colonne pour un objet

if opération == 'acheter' : 
    pains = int(input('pains ? '))
    bananes = int(input('bananes ? '))
    oeufs = int(input('oeufs  ? '))
    bières = int(input('bières ? '))

    
    choix = np.matrix([
        [pains],
        [bananes],
        [oeufs],
        [bières]
        ])
    totaux = prix * choix 
    print(totaux)                       #1x4 et une 4x3, en résulte une 1x3 (chaque total pour chaque magasin)
    min = 9999999
    for elem in totaux : 
        if elem < min :     # parcourir différemment peut être, avec une méthode propre aux matrices 
            min = float(elem) 
    print(min)

elif opération == 'verif' :  # Permet, en indicant les prix payés dans chaque magasin de retrouver quelle quantité d'objets on a acheté. Ici servira de vérification
    #Note = input(' Payé ? ')
    Maga1 = input('Payé  Magasin 1 ? ')
    Maga2 = input('Payé  Magasin 2 ? ')
    Maga3 = input('Payé  Magasin 3 ? ')
    Maga4 = input('Payé  Magasin 4 ? ')
    #Magasins = ['Delhaize', 'Carrefour', 'Colruyt']
    #i = Magasins.index(Magasin)
    a = np.array([
        [1, 1.5, 3, 6],
        [0.75,1.25, 4.3, 5.5],
        [1.3, 1.6,2.5,7.5],
        [2, 1, 4, 8]
        ], dtype='float')
    print(type(a))
    b = np.array([Maga1, Maga2, Maga3, Maga4],dtype='float')
    x= np.linalg.solve(a,b)
    print(x)


    

    








#Faire de 2 manières différentes ?  


# Programme pour optimiser achats d'une personne
# référence : https://www.mff.cuni.cz/veda/konference/wds/proc/pdf06/WDS06_106_m8_Ulrychova.pdf