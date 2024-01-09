'''
Module emission RMT sur ESP32
recoit une trame au format RMT 
Exemple : Trame_DMX_RMT_Rouge=(88, 8, 36, 8, 4, 40, 4, 40, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8) 

Paramètre de la sortie et de la vitesse

'''
#bibliothèque esp32 pour utiliser la fonction RMT
import esp32
from machine import Pin

#initilialisation de la sortie RMT pour le DMX
r = esp32.RMT(2, pin=Pin(18), clock_div=80)
print(r.source_freq()) # debug affichage vitesse 4uS

#fonction envoi signal RMT (DMX)
def emission_trame_DMX_RMT(trame_DMX_RMT) :
    r.write_pulses(trame_DMX_RMT, 0)
    


#Fonction main pour test autonome
def main() :
    Trame_DMX_RMT_Rouge=(88, 8, 36, 8, 4, 40, 4, 40, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8, 36, 8)
    trame_DMX_RMT = Trame_DMX_RMT_Rouge
    while True :
        emission_trame_DMX_RMT(trame_DMX_RMT)

if __name__ =="__main__" :
    main()


    