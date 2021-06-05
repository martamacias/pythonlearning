# es digitalitza el Dividend, el Divisor, el Quocient i el Residu
# El programa haurà de dir quines divisions són incorrectes i quines correctes


def calcular():
    print("Per acabar el programa escriu -1 al dividend")
    dividend = int(input("Dividend: "))
    while dividend != -1:
        divisor = int(input("Divisor: "))
        quocient = int(input("Quocient: "))
        residu = int(input("Residu: "))
        if (quocient, residu) == divmod(dividend, divisor):
            print("La divisió és correcte")
        else:
            print("La divisió és incorrecte")
        dividend = int(input("Dividend: "))


# Main
calcular()
