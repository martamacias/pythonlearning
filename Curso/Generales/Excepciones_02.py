# Capturar varias excepciones a la vez
def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print("La división es:", op1/op2)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except ValueError:
        print("El valor es erróneo")

    print("Operación finalizada")

# divide()


# Capturar excepciones en general (poco recomendado, aunque el programa no cae)
def divide_general():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print("La división es:", op1/op2)
    except:
        print("Ha ocurrido un error")

    print("Operación finalizada")

# divide2()

# sin el except, donde te indica el error pero el finally se ejecuta también
def divide_finally():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print("La división es:", op1/op2)
    finally: # el código que sigue se ejecuta SIEMPRE, da igual el error
        print("Operación finalizada")

divide_finally()
# el try tiene que tener except o finally