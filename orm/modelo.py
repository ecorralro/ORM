import random

# Creo clase jugador
class Jugador():
    def __init__(self):
        self.posx = random.randint(0,720)
        self.posy = random.randint(0,720)
        self.radio = 25
        self.direccion = random.randint(0,360)
        self.entidad = ""

# Creo la clase equipo, que hereda de la clase Jugador
class Equipo(Jugador):
    def __init__(self,posx,posy,radio,direccion,entidad):
        super().__init__(posx,posy,radio,direccion,entidad)
        self.color = random.choice()