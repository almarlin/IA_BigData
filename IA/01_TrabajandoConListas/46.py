nombres = list(["Alvaro", "Carla", "Estrella", "Francisco", "Javier"])


def empiezaVocal(nombre):
    return nombre[0].lower() in "aeiou"


vocales = list(filter(empiezaVocal, nombres))

print("Todos los nombres: ", nombres)
print("Los que empiezan por vocal: ", vocales)
