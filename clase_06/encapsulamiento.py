class Coche:

    def __init__(self, marca, modelo, color) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color #atributo privado. Se puede usar, pero por convencion no

#publicos
    def obtener_marca(self):
        return self.__marca

    def obtener_modelo(self):
        return self.__modelo
    
    def obter_color(self):
        return self.__color
    
#metodos privados
    def __acelerar(self):
        pass
    
coche = Coche("Toyota", "Modelo", "rojo")
print(coche.__color)
coche.__acelerar()