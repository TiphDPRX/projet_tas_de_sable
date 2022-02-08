############################
# groupe MI 2
# Tiphanie DEPREAUX
# Ania AOUAOUCHE
# Delphine HEMMERY
# https://github.com/uvsq22102500/projet_tas_de_sable
###########################

############### Constantes
HEIGHT = 500
WIDTH = 500

########### Partie Principale
import tkinter as tk
from tkinter.messagebox import YES

print("hello world")
racine = tk.Tk()
racine.title("Tas de Sable")
racine.geometry("600x600")
canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH)
canvas.pack(expand = YES)
racine.mainloop()

