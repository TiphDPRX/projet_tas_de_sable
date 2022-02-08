############################
# groupe MI 2
# Tiphanie DEPREAUX
# Ania AOUAOUCHE
# Delphine HEMMERY
# https://github.com/uvsq22102500/projet_tas_de_sable
###########################

############### 
# Librairies
import tkinter as tk

############### 
# Constantes
HEIGHT = 500
WIDTH = 500
N = 3

############## 
# Fonctions
def grille():
    grille = []
    for i in range(N):
        grille.append([0]*N)
    print(grille)


############
# Partie Principale

racine = tk.Tk()
racine.title("Tas de Sable")
racine.geometry("600x600")
canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH)
canvas.pack()


racine.mainloop()

