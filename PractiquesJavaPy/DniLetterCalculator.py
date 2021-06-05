# Donat el número d'un dni, es pot calcular la lletra
# L'usuari introduirà el número del dni
# Imprimeix el dni amb lletra inclosa
lletres = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z",
           "S", "Q", "V", "H", "L", "C", "K", "E"]


def input_dni():
    dni = int(input("Introdueix el dni sense lletra: "))
    return dni


def calcular_lletra():
    dni = input_dni()
    number = dni % 23
    lletra = lletres.__getitem__(number)
    print(str(dni)+lletra)


# Main
calcular_lletra()
