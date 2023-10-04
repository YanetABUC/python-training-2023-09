mi_dict = {
    "clave1": "valor 1",
    "clave2": "valor 2",
    "clave1": "valor 3"
}

mi_dict["clave3"] = "valor 4"

print(mi_dict)
print(mi_dict.keys())
print(mi_dict.items())
print(mi_dict.values())

print(mi_dict.get("clave_no_existe", "default_value"))
