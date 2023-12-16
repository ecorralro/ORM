import json
import random
import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


personas = []
numeropersonas = 5
colores = ["red","blue","green","yellow","orange","black","white","pink"]

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
        elif self.color == "orange":
            return 15
        elif self.color == "black":
            return 5
        elif self.color == "white":
            return 20
        elif self.color == "pink":
            return 12
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
            INSERT OR REPLACE INTO jugadores
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
# Creo nueva ventana para consultas
def ventana_consultas():
    ventana_consultas =tk.Toplevel(raiz,padx=60,pady=60,background="grey")
    ventana_consultas.title("Consultas")
    estilo=ttk.Style()
    estilo.theme_use('clam')
    estilo.configure('TLabel', background='#ffd699', font=('Arial', 12, 'bold'))
    estilo.configure('TButton')
    estilo.configure('Boton_rojo.TButton',background="red",foreground="red")
    estilo.configure('Boton_azul.TButton',background="blue",foreground="blue")
    estilo.configure('Boton_verde.TButton',background="green",foreground="green")
    estilo.configure('Boton_amarillo.TButton',background="yellow",foreground="yellow")
    estilo.configure('Boton_naranja.TButton',background="orange",foreground="orange")
    estilo.configure('Boton_negro.TButton',background="black",foreground="black")
    estilo.configure('Boton_blanco.TButton',background="white",foreground="white")
    estilo.configure('Boton_rosa.TButton',background="pink",foreground="pink")

    label_consulta = ttk.Label(ventana_consultas, text="Cuantos jugadores hay del color:",style='TLabel')
    label_consulta.grid(row=0, column=0,columnspan=4, padx=5, pady=5, sticky=tk.N)

    boton_rojo=ttk.Button(ventana_consultas,style='Boton_rojo.TButton',text="Rojo",command=lambda:consulta_personas_color("red"))
    boton_rojo.grid(row=1,column=0, padx=5, pady=5, sticky=tk.W)
    boton_azul=ttk.Button(ventana_consultas,style='Boton_azul.TButton',text="Azul",command=lambda:consulta_personas_color("blue"))
    boton_azul.grid(row=1,column=1, padx=5, pady=5, sticky=tk.W)
    boton_verde=ttk.Button(ventana_consultas,style='Boton_verde.TButton',text="Verde",command=lambda:consulta_personas_color("green"))
    boton_verde.grid(row=1,column=2, padx=5, pady=5, sticky=tk.W)
    boton_amarillo=ttk.Button(ventana_consultas,style='Boton_amarillo.TButton',text="Amarillo",command=lambda:consulta_personas_color("yellow"))
    boton_amarillo.grid(row=1,column=3, padx=5, pady=5, sticky=tk.W)
    boton_naranja=ttk.Button(ventana_consultas,style='Boton_naranja.TButton',text="Naranja",command=lambda:consulta_personas_color("orange"))
    boton_naranja.grid(row=2,column=0, padx=5, pady=5, sticky=tk.W)
    boton_negro=ttk.Button(ventana_consultas,style='Boton_negro.TButton',text="Negro",command=lambda:consulta_personas_color("black"))
    boton_negro.grid(row=2,column=1, padx=5, pady=5, sticky=tk.W)
    boton_blanco=ttk.Button(ventana_consultas,style='Boton_blanco.TButton',text="Blanco",command=lambda:consulta_personas_color("white"))
    boton_blanco.grid(row=2,column=2, padx=5, pady=5, sticky=tk.W)
    boton_rosa=ttk.Button(ventana_consultas,style='Boton_rosa.TButton',text="Rosa",command=lambda:consulta_personas_color("pink"))
    boton_rosa.grid(row=2,column=3, padx=5, pady=5, sticky=tk.W)

    ventana_consultas.mainloop()

def consulta_personas_color(color):
    conexion = sqlite3.connect("jugadores.sqlite3")
    cursor =conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM jugadores WHERE color=?',(color,)) # (color,) para q el valor se pase cómo una tupla y no pete

    resultado = cursor.fetchone()
    if resultado is not None:
        cantidad_personas = resultado[0]
        mensaje = f"Hay {cantidad_personas} jugadores del color {color}"
        messagebox.showinfo("Consulta", mensaje)
    else:
        messagebox.showinfo("Consulta", f"No hay jugadores del color {color}")

    conexion.commit()
    conexion.close()




# Creo ventana
raiz = tk.Tk()
raiz.title("Jugadores")
# Creo un lienzo en esa ventana
lienzo = tk.Canvas(raiz,width=720,height=720,background="grey")
lienzo.pack()

# creo un botón para guardar
boton = ttk.Button(raiz, text="Guardar",command = guardar_personas)
boton.pack(side=tk.LEFT,padx=5)
boton_agregar = ttk.Button(raiz, text="+ 5",command=agregar_personas)
boton_agregar.pack(side=tk.LEFT,padx=5)
boton_consultas = ttk.Button(raiz, text="Consultas",command=ventana_consultas)
boton_consultas.pack(side=tk.LEFT,padx=5)
# Cargar personas existentes desde el archivo
'''
**CARGO DESDE UN .JSON**
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
'''
# Cargar personas desde base de datos
conexion = sqlite3.connect("jugadores.sqlite3")
cursor = conexion.cursor()

try:
    # Ejecutar una consulta para obtener los datos de la base de datos
    cursor.execute('SELECT * FROM jugadores') 
    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()
    # Recorrer los resultados y crear objetos Persona
    for resultado in resultados:
        persona = Persona()
        persona.id,persona.posx, persona.posy, persona.color, persona.radio, persona.direccion, persona.entidad = resultado
        personas.append(persona)
except sqlite3.Error as e:
    print("Error al cargar desde la base de datos:", e)
finally:
    # Cerrar la conexión a la base de datos
    conexion.close()
    
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