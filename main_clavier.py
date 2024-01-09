'''
projecteur1 : canaux  DMX1 à DMX4 
Saisie des valeurs
modification de la trame_DMX_DEC et
modification trame _DMX_RMT

emission en continue
'''

import emission_RMT
import conception_trame_RMT
        
def main():
    #trame_DMX_DEC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #trame_DMX_RMT = [88, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8]
    #programme principal
    w = int(input("Donnez l'intensité générale du projecteur 1 entre 0 et 255  : "))
    r = int(input("Donnez l'intensité de la composante rouge du projecteur 1 entre 0 et 255  : "))
    g = int(input("Donnez l'intensité de la composante verte du projecteur 1 entre 0 et 255  : "))
    b = int(input("Donnez l'intensité de la composante bleue du projecteur 1 entre 0 et 255  : "))
    trame_DMX_DEC = [w,r,g,b]
    print(trame_DMX_DEC)
    trame_DMX_RMT = conception_trame_RMT.conception_trame_DMX_RMT(trame_DMX_DEC)  
    while True :
        emission_RMT.emission_trame_DMX_RMT(trame_DMX_RMT)

if __name__ =="__main__" :
    main()



