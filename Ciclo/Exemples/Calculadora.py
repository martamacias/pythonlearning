# Marta Macias Gordon
# 26/04/2021


import math


def suma():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    total = x + y
    print("Resultat: ", total)
    input("Enter per continuar...")


def resta():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    total = x - y
    print("Resultat: ", total)
    input("Enter per continuar...")


def multipl():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    total = x * y
    print("Resultat: ", total)
    input("Enter per continuar...")


def divisio():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    total = x / y
    print("Resultat: ", total)
    input("Enter per continuar...")


def absolute():
    input("Introdueix el numero: ")
    x = float(input())
    total = abs(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def divquo():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    print("Resultat: ", divmod(x, y))
    input("Enter per continuar...")


def pownum():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    print("Resultat: ", pow(x, y))
    input("Enter per continuar...")


def modul():
    input("Introdueix els numeros: ")
    x = float(input())
    y = float(input())
    print("Resultat: ", math.fmod(x, y))
    input("Enter per continuar...")


def arrel_quadrada():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.sqrt(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def acos():
    input("Introdueix el numero (-1 a 1): ")
    x = float(input())
    total = math.acos(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def asin():
    input("Introdueix el numero (-1 a 1): ")
    x = float(input())
    total = math.asin(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def atan():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.atan(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def cos():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.cos(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def sin():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.sin(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def tan():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.tan(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def graus():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.degrees(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def radians():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.radians(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def acosh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.acosh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def asinh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.asinh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def atanh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.atanh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def cosh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.cosh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def sinh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.sinh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def tanh():
    input("Introdueix el numero: ")
    x = float(input())
    total = math.sinh(x)
    print("Resultat: ", total)
    input("Enter per continuar...")


def pi():
    total = math.pi
    print("Resultat: ", total)
    input("Enter per continuar...")


def econst():
    total = math.e
    print("Resultat: ", total)
    input("Enter per continuar...")


def menu_calculadora():
    while True:
        print("***************\n"
              "     Menu      \n"
              "***************\n"
              "1. Suma\n"
              "2. Resta\n"
              "3. Multiplicacio\n"
              "4. Divisio\n"
              "5. Numero absolut\n"
              "6. Divisio quocient i resta\n"
              "7. Potencia\n"
              "8. Modul\n"
              "9. Arrel quadrada\n"
              "10. Acos\n"
              "11. Asin\n"
              "12. Atan\n"
              "13. Cos\n"
              "14. Sin\n"
              "15. Tan\n"
              "16. De radians a graus\n"
              "17. De graus a radians\n"
              "18. Acosh\n"
              "19. Asinh\n"
              "20. Atanh\n"
              "21. Cosh\n"
              "22. Sinh\n"
              "23. Tanh\n"
              "24. Numero pi\n"
              "25. Constant e\n"
              "0. Finalitzar\n")
        option = input("Metode a fer: ")
        if option == '1':
            suma()
        elif option == '2':
            resta()
        elif option == '3':
            multipl()
        elif option == '4':
            divisio()
        elif option == '5':
            absolute()
        elif option == '6':
            divquo()
        elif option == '7':
            pownum()
        elif option == '8':
            modul()
        elif option == '9':
            arrel_quadrada()
        elif option == '10':
            acos()
        elif option == '11':
            asin()
        elif option == '12':
            atan()
        elif option == '13':
            cos()
        elif option == '14':
            sin()
        elif option == '15':
            tan()
        elif option == '16':
            graus()
        elif option == '17':
            radians()
        elif option == '18':
            acosh()
        elif option == '19':
            asinh()
        elif option == '20':
            atanh()
        elif option == '21':
            cosh()
        elif option == '22':
            sinh()
        elif option == '23':
            tanh()
        elif option == '24':
            pi()
        elif option == '25':
            econst()
        elif option == '0':
            break
        else:
            print("Opcio incorrecta, torna a provar...")


# Main
menu_calculadora()
