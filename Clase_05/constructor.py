class Car:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        print(f"Vehiculo {marca} {modelo} creado.")

    def __del__(self):
        print(f"Vehiculo {self.marca} {self.modelo} destruido.")

    def __str__(self) -> str:
        return "Hola este es un auto de la marca " + self.marca

mi_coche = Car("Toyota", "Corolla")
mi_coche = Car("Toyota1", "Corolla11")

print(mi_coche)
mi_coche.marca = "La cambie"
print(mi_coche)
del mi_coche