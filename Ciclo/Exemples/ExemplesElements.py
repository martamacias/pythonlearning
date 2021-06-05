# Marta Macias Gordon
# 15/05/2021


def llistes_iguals():
    print("Comparador de llistes")
    print("LLista 1")
    llista1 = input_list()
    print("LLista 2")
    llista2 = input_list()

    def compara_llistes():
        compare = False
        x = len(llista1)
        y = len(llista2)
        if x == y:
            for i in range(0, x):
                if llista1[i] == llista2[i]:
                    compare = True
                else:
                    compare = False
                    break
        else:
            compare = False
        return compare

    equals_list = compara_llistes()
    if equals_list:
        print("Les llistes són iguals")
    else:
        print("Les llistes no són iguals")
    input("Enter per continuar...")


def suma_matriu():
    print("Sumar els elements de les files i després de les columnes de una matriu")
    n = int(input("Número de files: "))
    m = int(input("Número de columnes: "))
    matriu = input_matriu(n, m)
    print("La matriu és:", matriu)

    def sumar_files():
        suma_files = []
        for fila in matriu:
            x = 0
            for valor in fila:
                x = x+valor
            suma_files.append(x)
        return suma_files

    files = sumar_files()
    print("La suma de les files és:", files)

    def sumar_columnes():
        suma_column = []
        for i in range(n):
            y = 0
            for j in range(m):
                y = y+matriu[j][i]
            suma_column.append(y)
        return suma_column

    columnes = sumar_columnes()
    print("La suma de les columnes és:", columnes)
    input("Enter per continuar...")


def numero_primer():
    print("Comprobar si un número és primer")
    num = int(input("Número a comprobar: "))
    primer = False
    for n in range(2, num):
        if num % n == 0:
            primer = True
            break
    if primer:
        print("No és primer")
    else:
        print("És primer")


def mult_infinits():
    print("Retorna un llista infinita amb els múltiples d'un número")
    num = int(input("Número: "))
    lista = []
    while True:
        num = num+num
        lista.append(num)
        print(lista)


# Input
def input_list():
    lista = []
    x = int(input("Numero d'elements de la llista:"))
    for i in range(0, x):
        element = input()
        lista.append(element)
    return lista


def input_matriu(n, m):
    matriu = []
    print("Elements de la matriu: ")
    for i in range(n):
        matriu.append([])
        for j in range(m):
            matriu[i].append(int(input()))
    return matriu


# Menu
def menu_elements():
    while True:
        print("***************\n"
              "     Menu      \n"
              "***************\n"
              "0. Sortir\n"
              "1. Llistes iguals\n"
              "2. Suma de matriu\n"
              "3. És número primer\n"
              "4. Múltiples infinits\n")
        option = input("Funció a fer: ")
        if option == '0':
            break
        elif option == '1':
            llistes_iguals()
        elif option == '2':
            suma_matriu()
        elif option == '3':
            numero_primer()
        elif option == '4':
            mult_infinits()
        else:
            print("Opcio incorrecta, torna a provar...")


# Main
menu_elements()
