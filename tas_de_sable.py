############################
# groupe MI 2
# Tiphanie DEPREAUX
# Ania AOUAOUCHE
# Delphine HEMMERY
# https://github.com/uvsq22102500/projet_tas_de_sable
###########################

# importation des bibliotheques 
from sys import builtin_module_names
from tkinter import *
import random

#creation de la taille de notre canvas
height=800
width=800

# creation de nos variables globales
liste_chiffre=[]
liste=[]


#creation de l'interface graphique (notre fenetre et canvas) 
window=Tk()
window.title("tas de sable")
window.geometry("800x800")
canvas=Canvas(window, height=height , width=width)
#faire appel a notre fonction qui demarera tout notre programme


#####################FUNCTIONS######################

#fonction qui va creer la configuration courante (sans les chiffres)

def config_courante():
    chiffre1 = Label(window, text="#")
    chiffre2 = Label(window, text="#")
    chiffre3 = Label(window, text="#")
    chiffre4 = Label(window, text="#")
    chiffre5 = Label(window, text="#")
    chiffre6 = Label(window, text="#")
    chiffre7 = Label(window, text="#")
    chiffre8 = Label(window, text="#")
    chiffre9 = Label(window, text="#")
    '''affichage des # '''

    #mettre les chiffres dans une liste a 2D
    liste_chiffre=[chiffre1,chiffre2,chiffre3,chiffre4,chiffre5,chiffre6,chiffre7,chiffre8,chiffre9]

    #creer une liste composée aleatoirement
    for i in range (9):
        n= random.randint (1,9)
        liste.append(n)

#fonction couleurs 
''' chaque chiffre aura une couleur ? '''
    
    liste_chiffre[0]=blue 
    liste_chiffre[1]=green 
    liste_chiffre[2]=red 
    liste_chiffre[3]=orange 
    liste_chiffre[4]=yellow
    liste_chiffre[5]=cyan 
    liste_chiffre[6]=magenta
    liste_chiffre[7]=white 
    liste_chiffre[8]=black 

#config aleatoire entre 0 3
'''pas compris'''



#fonction du bouton qui vas creer les 9 chiffres initiales
def config_courante2():
    for i in range (9):
        liste_chiffre[i].config(text=str(liste[i]))
    '''liste_chiffre[i]=liste[i] '''
    ''' affichage... '''
     
#creation du bouton et son affichage
boutton=Button(window, command=config_courante2 , text='Generer')
boutton.pack()



# fonction addition et son boutton
def addition():
    for i in range(9):
        liste_chiffre[i]+=liste_chiffre[i]
        '''int si besoin et l affichage'''

boutton_add=Button(window,command=addition)

# fonction soustraction et son boutton
def soustraction():
    for i in range(9):
        liste_chiffre[i]-=liste_chiffre[i]
        '''int si besoin et l affichage'''

boutton_sou=Button(window,command=soustraction)
 
#faire une etape de l'automate
#calculer la stabilisation d'une config

'''faire appel a config_courante'''
window.mainloop()





