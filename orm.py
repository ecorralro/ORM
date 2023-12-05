import random
import tkinter as tk



# Creo objeto persona
class Persona():
    def __init__(self):
        self.posx = random.randint(0,720)
        self.posy = random.randint(0,720)
        self.color = "red"
        self.radio = 25
        self.direccion = random.randint(0,360)
        self.entidad = ""
# Dibujo en el lienzo
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx - self.radio/2,
            self.posy - self.radio/2,
            self.posx + self.radio/2,
            self.posy + self.radio/2,
            fill = self.color)

# Creo ventana
raiz = tk.Tk()
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=720,height=720)
lienzo.pack()

persona = Persona()      
Persona.dibuja(persona)


raiz.mainloop()