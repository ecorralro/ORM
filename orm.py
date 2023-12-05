import random
import tkinter as tk

# Creo ventana
raiz = tk.Tk()
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

raiz.mainloop()

# Creo objeto persona
class Persona():
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.color = "red"
        self.radio = 25
        self.direccion = random.randint(0,360)
        