def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2): # Error dividir con 0
    try:
        return num1 / num2
    except ZeroDivisionError: # Nombre del error
        print("No se puede dividir entre 0")
        return "Operación errónea" # después el programa continúa

while True: # bucle hasta que se introduzcan bien y salga con el break
    try: # valores introducidos inválidos
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break
    except ValueError: # nombre del error
        print("El elemento debe ser un entero. Inténtalo de nuevo.")

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

# Queremos que esta linea se ejecute aunque hayan errores
print("Operación ejecutada. Continuación de ejecúción del programa ")