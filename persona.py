class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrarDatos(self):
        print("=== DATOS PERSONALES ===")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)