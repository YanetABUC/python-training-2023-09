class Gato:
    color = "Negro"

    #constructor
    def __init__(self) -> None:
        pass

    def maullar(self):
        print("Miau!")

    #Destructor
    def __del__(self):
        pass


mi_gato = Gato()
print(mi_gato.color)
mi_gato.color = "Blanco"
print(mi_gato.color)
mi_gato.maullar()