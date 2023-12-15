import json
import random
import math
import tkinter as tk
from tkinter import ttk
import sqlite3


personas = []
numeropersonas = 5
colores = ["red","blue","green","yellow"]

# Creo objeto persona
class Persona():
    def __init__(self):
        self.posx = random.randint(0,720)
        self.posy = random.randint(0,720)
        self.color = random.choice(colores)
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
            math.cos(self.direccion) * self.velocidad_color(),
            math.sin(self.direccion) * self.velocidad_color()
            )
        self.posx += math.cos(self.direccion) * self.velocidad_color()
        self.posy += math.sin(self.direccion) * self.velocidad_color()
    def rebote(self):
        if self.posx < 0 or self.posx > 720 or self.posy < 0 or self.posy > 720:
            self.direccion += math.pi
    # Velocidad según color
    def velocidad_color(self):
        if self.color == "red":
            return 1
        elif self.color == "blue":
            return 30
        elif self.color == "green":
            return 10
        elif self.color == "yellow":
            return 100
# Creo un bucle para que esas personas se muevan
def bucle():
    for persona in personas:
        persona.mueve()
    raiz.after(10,bucle)

def agregar_personas():
    for _ in range(5):
        nueva_persona = Persona()
        nueva_persona.dibuja()
        personas.append(nueva_persona)
            
def guardar_personas():
    '''    
    **GUARDADO EN .JSON**
    cadena = json.dumps([vars(persona) for persona in personas])
    archivo = open("jugadores.json",'w')
    archivo.write(cadena)
    archivo.close()
 '''
    conexion = sqlite3.connect("jugadores.sqlite3")
    cursor =conexion.cursor()
    for persona in personas:
        cursor.execute('''
            INSERT INTO jugadores
            VALUES (
                NULL,
                '''+str(persona.posx)+''',
                '''+str(persona.posy)+''',
                "'''+str(persona.color)+'''",
                '''+str(persona.radio)+''',
                '''+str(persona.direccion)+''',
                "'''+str(persona.entidad)+'''"         
            )
            ''')
    conexion.commit()
    conexion.close()



# Creo ventana
raiz = tk.Tk()
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=720,height=720,background="grey")
lienzo.pack()

# creo un botón para guardar
boton = ttk.Button(raiz, text="Guardar",command = guardar_personas)
boton.pack()
botonadd = ttk.Button(raiz, text="+ 5",command=agregar_personas)
botonadd.pack(pady=5)
# Cargar personas existentes desde el archivo
try:
    carga = open("jugadores.json",'r')
    cargado = carga.read()
    cargado_lista = json.loads(cargado)
    for elemento in cargado_lista:
        persona = Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)
except:
    print("error")
    
# Creo todo el número de personas y las dibujo
if len(personas) == 0:
    numeropersonas = 5
    for i in range(0,numeropersonas):
        personas.append(Persona())
for persona in personas:
    persona.dibuja()

# LLamamos a función bucle
bucle()
        
raiz.mainloop()