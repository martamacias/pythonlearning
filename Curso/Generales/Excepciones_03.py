# Excepción propia
import math


def calcula_raiz(num1):
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")  # Error no capturado, solo definido
    else:
        return math.sqrt(num1)


op1 = (int(input("Introduce un número: ")))

try:
    print(calcula_raiz(op1))
except ValueError as ErrorNumeroNegativo:  # se puede poner un alias
    print(ErrorNumeroNegativo)

# hay que capturar la excepción para que el programa siga
print("Programa finalizado")
