'''
Module permettant de concevoir les signaux RMT à partir
d'une trame_DMX_DEC c'est à dire contenant les valeurs de chaque canal
exemple trame_DMX_DEC=[150,20,0,0,255,0,0,0,0,0,0,0,0,0,0,0]#1

sortie : signal trame_DMX_RMT
exemple : trame_DMX_RMT =[88, 8, 36, 8, 8, 8, 4, 4, 8, 12, 12, 4, 4, 4, 12, 8, 36, 8, 36, 8, 4, 40, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8]
'''

def conception_trame_DMX_RMT(trame_DMX_DEC) : 
    #Conception trame_DMX_str 
    Break='0000000000000000000000'#88ms
    MAB='11' # Mark After Break
    code_depart ='00000000011'#1bit start + value=0 + 2bits stop
    trame_DMX_str=Break+MAB+code_depart
    for i in range (0, len(trame_DMX_DEC)):
        trameX='0'#start
        for masque in [1,2,4,8,16,32,64,128]:
           if (trame_DMX_DEC[i]&masque != 0) :
               trameX=trameX+'1'
           else :
               trameX=trameX+'0'
        trameX=trameX+'11'# 2 bits stop
        trame_DMX_str=trame_DMX_str+trameX
    print(trame_DMX_str)
    print(len(trame_DMX_str))#calcul-26-11 = -37

    #Conception trame_DMX_RMT à partir du découpage de trame_DMX_str
    trame_DMX_RMT=[] # liste des durées Etats haut puis Etats bas 
    nb=0
    lectureprecedente='0'
    # nbmot=len(trameDMXstr)
    for i in range (0,len(trame_DMX_str)):
        if trame_DMX_str[i]==lectureprecedente:
            nb=nb+4 # 4us = 250kHz
        else :
            trame_DMX_RMT.append(nb)
            lectureprecedente=trame_DMX_str[i]
            nb=4 #4us = 250kHz
    trame_DMX_RMT.append(nb)
    print (trame_DMX_RMT)
    return(trame_DMX_RMT)


#Fonction main pour test autonome
def main() :
    trame_DMX_DEC=[255,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0]#1 
    trame_DMX_RMT = conception_trame_DMX_RMT(trame_DMX_DEC)
    print (trame_DMX_RMT)
   
if __name__ =="__main__" :
    main()
