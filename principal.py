from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

print("==============================")
print("    SISTEMA DE UNIVERSIDAD")
print("==============================")

#Crea estudiante
estudiante1 = Estudiante("Ana", 22, "Ingeniería Informática")
#Crear profesor
profesor1 = Profesor("Carlos", 45, "Programación")
#Crear curso
curso1 = Curso("Programación en Python", 4)

#Mostrar información
print("INFORMACIÓN DEL ESTUDIANTE\n")
estudiante1.mostrarDatos()
estudiante1.matricular()
print("\n")

print("INFORMACIÓN DEL PROFESOR\n")
profesor1.mostrarDatos()
profesor1.impartirClase()
print("\n")

curso1.mostrarCurso()