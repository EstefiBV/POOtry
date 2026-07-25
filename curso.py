class Curso:
    def __init__(self, nombreCurso, creditos):
        self.nombreCurso = nombreCurso
        self.creditos = creditos
    def mostrarCurso(self):
        print("=== CURSO ===")
        print("Nombre: ", self.nombreCurso)
        print("Créditos: ", self.creditos)