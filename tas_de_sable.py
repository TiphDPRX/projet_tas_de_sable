############################
# groupe MI 2
# Ania AOUAOUCHE
# Tiphanie DEPREAUX
# Delphine HEMMERY
# https://github.com/uvsq22102500/projet_tas_de_sable
###########################

# importation des bibliotheques 
from tkinter import *
import random


#creation de la taille de notre canvas
height=600
width=600


# creation de nos variables globales
liste=[]
liste_G=[]
N=12
''' liste est une liste qu'on utilisera comme sous liste afin de creer notre liste_G de 2Dimensions 
quant a N c est le nombre de cases qu'on generera soit NxN '''


#creation de notre fenetre principale 
window=Tk()
window.title("tas de sable")
window.geometry("700x700")
canvas=Canvas(window, height=height , width=width)
canvas.pack(expand=YES) 


###############################FUNCTIONS##################################


#fonction qui va creer la configuration courante 
def config_courante():
    #creation de la grille
    for i in range (N):
        for j in range (N):
            canvas.create_rectangle((50*i,50*j), ( (50*(i+1)),(50*(j+1)) ),fill='black')
    
    #creation de ma liste a 2D 
    for x in range (N):
        liste=[]
        for y in range (N):   
            a = random.randint(1,9)
            liste.append(a)
        liste_G.append(liste)



#fonction qui va associer chaque chiffre a une couleur 
def couleur() :
    for i in range (N):
        for j in range (N):
            if liste_G[i][j] == 1 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="red")
            elif liste_G[i][j] == 2 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="blue")
            elif liste_G[i][j] == 3 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="green")
            elif liste_G[i][j] == 4 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="black")
            elif liste_G[i][j] == 5 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="white")
            elif liste_G[i][j] == 6 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="yellow")
            elif liste_G[i][j] == 7 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="purple")
            elif liste_G[i][j] == 8 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="pink")         
            elif liste_G[i][j] == 9 :
                canvas.create_rectangle((50*j , 50*i),( (50*(j+1)) , (50*(i+1)) ), fill ="brown")


#faire appel a la fonctiion config_courante avant la fonction couleur
config_courante()
#creation du bouton de generation de notre terrain et son affichage
boutton=Button(window, command=couleur , text='Generer',bg='black', fg='white')
boutton.pack()

#creation de la fonction qui va creer l'eboulement
def eboulement():
    

#creation du bouton qui permettra de faire l'eboulement
boutton_eboulement=Button(window, command=eboulement ,text='eboulement' , bg='black', fg='white')
boutton_eboulement.pack()


window.mainloop()





