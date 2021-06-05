# Marta Macias Gordon
# 19/04/2021


def exemple_abs():
    print("Mètode abs per retornar el valor absolut de un número: ")
    print("El número és -5.")
    number = abs(-5)
    print("Número absolut és:", number)
    input("Enter per continuar...")


def exemple_all():
    print("Metode all que retorna true si tots els elements tenen valor True o esta buit. False en el cas contrari: ")
    llista = [0, 1, 3]
    print("Llista: ", llista, all(llista))
    llista2 = [False, True]
    print("Llista: ", llista2, all(llista2))
    llista3 = [True, 3, "hola"]
    print("Llista: ", llista3, all(llista3))
    llista4 = []
    print("Llista: ", llista4, all(llista4))
    input("Enter per continuar...")


def exemple_any():
    print("Metode any que retorna true si la llista té alguns elements true. False en el cas contrari o si està buit:")
    llista = [0, 1, 3]
    print("Llista: ", llista, any(llista))
    llista2 = [False, False]
    print("Llista: ", llista2, any(llista2))
    llista3 = [True, False, "hola"]
    print("Llista: ", llista3, any(llista3))
    llista4 = []
    print("Llista: ", llista4, any(llista4))
    input("Enter per continuar...")


def exemple_bin():
    print("Metode bin que retorna el número binar corresponent a un número enter:")
    number = 62
    print("Numero:", number, "Binari:", bin(number))
    input("Enter per continuar...")


def exemple_bool():
    print("Metode bool que retorna 0 si és false i 1 en cas contrari:")
    x = False
    print("Variable:", x, "| Bool:", bool(x))
    x = True
    print("Variable:", x, "| Bool:", bool(x))
    x = 0
    print("Variable:", x, "| Bool:", bool(x))
    x = "hola"
    print("Variable:", x, "| Bool:", bool(x))
    input("Enter per continuar...")


def exemple_chr():
    print("Metode chr que retorna el caracter corresponent a un codi ASCII")
    x = 77
    print("Caracter amb codi ASCII", x, ":", chr(x))
    input("Enter per continuar...")


def exemple_divmod():
    print("Metode divmod que retorna el quocient i el reste de la divisió de dos números no complexes:")
    print("Numeros 12 i 5. Divmod: ", divmod(12, 5))
    input("Enter per continuar...")


def exemple_enumerate():
    print("Metode enumerate per enumerar elements de una llista: ")
    values = ["a", "b", "c"]
    for counter, value in enumerate(values):
        print(counter, value)
    input("Enter per continuar...")


def exemple_eval():
    print("Metode eval que analitza una expressió des de un String i retorna el resultat: ")
    x = 1
    print("x = String", 1, "eval('x + 1') =", eval('x + 1'))
    input("Enter per continuar...")


def exemple_filter():
    print("Metode filter que retorna un iterable filtrat segons funció: ")
    values = ["l", 0, False, "hola", "0"]
    print("Llista:", values)
    filtered = filter(None, values)
    print("Valors no nuls:", list(filtered))
    input("Enter per continuar...")


def exemple_pow():
    print("Metode pow que retorna el resultat del primer numero elevat al segon:")
    x = 10
    y = 2
    print("Numeros:", x, y)
    print("Pow:", pow(x, y))
    input("Enter per continuar...")


def exemple_reversed():
    print("Metode reversed que retorna un iterable amb el ordre invertit:")
    values = ["l", 0, False, "hola", "0"]
    print("Llista inicial:", values)
    values2 = reversed(values)
    print("Llista amb reversed:", list(values2))
    input("Enter per continuar...")


def exemple_round():
    print("Metode round que arrodoneix un numero al sencer més proper:")
    x = 5.2
    print("Numero:", x)
    print("Round:", round(x))
    input("Enter per continuar...")


def exemple_max():
    print("Metode max que retorna el màxim valor de un iterable:")
    llista = [0, 1, 3, 5, 9, 4]
    print("LLista:", llista)
    print("Max:", max(llista))
    input("Enter per continuar...")


def exemple_min():
    print("Metode min que retorna el minim valor de un iterable:")
    llista = [0, 1, 3, 5, 9, 4]
    print("LLista:", llista)
    print("Min:", max(llista))
    input("Enter per continuar...")


def exemple_str():
    print("Metode str que retorna un string de un parametre:")
    llista = [0, 1, 3, 5, 9, 4]
    print("Amb una llista:", str(llista))
    print("Amb un numero:", str(56))
    input("Enter per continuar...")


def exemple_sum():
    print("Metode sum que retorna la suma dels elements de un iterable:")
    llista = [0, 1, 3, 5, 9, 4]
    print("Llista:", llista, "Suma:", sum(llista))
    input("Enter per continuar...")


def exemple_type():
    print("Metode type que retorna el tipus de objecte:")
    llista = [0, 1, 3, 5, 9, 4]
    print("Objecte:", llista, "Type:", type(llista))
    x = 'hola'
    print("Objecte:", x, "Type:", type(x))
    y = 50
    print("Objecte:", y, "Type:", type(y))
    input("Enter per continuar...")


def menu_funcions():
    while True:
        print("***************\n"
              "     Menu      \n"
              "***************\n"
              "1. Absolute number\n"
              "2. All iterable\n"
              "3. Any iterable\n"
              "4. Binary number\n"
              "5. Boolean return\n"
              "6. Char ASCII\n"
              "7. Divmod (quocient i resta)\n"
              "8. Enumerate\n"
              "9. Eval\n"
              "10. Filter\n"
              "11. Pow\n"
              "12. Reversed\n"
              "13. Round\n"
              "14. Max\n"
              "15. Min\n"
              "16. Str\n"
              "17. Sum\n"
              "18. Type\n"
              "0. Finalitzar\n")
        option = input("Metode a fer: ")
        if option == '1':
            exemple_abs()
        elif option == '2':
            exemple_all()
        elif option == '3':
            exemple_any()
        elif option == '4':
            exemple_bin()
        elif option == '5':
            exemple_bool()
        elif option == '6':
            exemple_chr()
        elif option == '7':
            exemple_divmod()
        elif option == '8':
            exemple_enumerate()
        elif option == '9':
            exemple_eval()
        elif option == '10':
            exemple_filter()
        elif option == '11':
            exemple_pow()
        elif option == '12':
            exemple_reversed()
        elif option == '13':
            exemple_round()
        elif option == '14':
            exemple_max()
        elif option == '15':
            exemple_min()
        elif option == '16':
            exemple_str()
        elif option == '17':
            exemple_sum()
        elif option == '18':
            exemple_type()
        elif option == '0':
            break
        else:
            print("Opcio incorrecta, torna a provar...")


# Main
menu_funcions()

# apply
# cmp
# compile
# delattr
# exec
# getattr
# hasattr
# open
# setattr
