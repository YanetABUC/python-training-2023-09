class Estudiante:
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} y estoy en {self.grado} grado")

juan = Estudiante("Juan", 12, "6to")
juan.presentarse()