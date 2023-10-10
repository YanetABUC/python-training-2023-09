def leer_archivo(nombre_archivo:str):
    """
    Este metodo permitira leer un archivo a partir del nombre que indique el usuario
    :param nombre_archivo : Indica el nombre del archivo que sera leido
    """
    try:
        with open(nombre_archivo, "r") as file:
            contenido = file.read()
            print(contenido)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

nombre_archivo = input("Indica el nombre del archivo a leer: ")
leer_archivo(nombre_archivo)