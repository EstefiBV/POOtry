from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def impartirClase(self):
        print(self.nombre, " imparte la asignatura de: ", self.especialidad)
