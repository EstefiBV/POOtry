#super().__init__() inicializamos todo los atributos heredados
from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def matricular(self):
        print(self.nombre, " se matriculó en la carrera de ", self.carrera )