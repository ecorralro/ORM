import random
import math
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
        self.rebote()
        lienzo.move(
            self.entidad,
            math.cos(self.direccion),
            math.sin(self.direccion)
            )
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def rebote(self):
        if self.posx < 0 or self.posx > 720 or self.posy < 0 or self.posy > 720:
            self.direccion += math.pi
def guardar_personas():
    print("Guardado")

# Creo ventana
raiz = tk.Tk()
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=720,height=720)
lienzo.pack()

# creo un botón para guardar
boton = tk.Button(raiz, text="Guardar",command = guardar_personas)
boton.pack()
# Creo todo el número de personas y las dibujo
for i in range(0,numeropersonas):
    personas.append(Persona())
for persona in personas:
    persona.dibuja()
# Creo un bucle para que esas personas se muevan
def bucle():
    for persona in personas:
        persona.mueve()
    raiz.after(10,bucle)

persona = Persona()      
Persona.dibuja(persona)
bucle()


raiz.mainloop()