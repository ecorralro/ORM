import random
import tkinter as tk

personas = []
numeropersonas = 20

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
    def mueve(self):
        lienzo.move(self.entidad,10,0)

# Creo ventana
raiz = tk.Tk()
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=720,height=720)
lienzo.pack()
# Creo todo el número de personas y las dibujo
for i in range(0,numeropersonas):
    personas.append(Persona())
for persona in personas:
    persona.dibuja()
# Creo un bucle para que esas personas se muevan
def bucle():
    for persona in personas:
        persona.mueve()
    raiz.after(100,bucle)

persona = Persona()      
Persona.dibuja(persona)
bucle()


raiz.mainloop()