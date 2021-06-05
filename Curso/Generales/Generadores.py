# LISTA SENCILLA CON GENERADOR
def generador_pares(limite):
    num = 0

    while num < limite:
        yield num+2
        num += 2


pares = generador_pares(10) # Estado de suspensión

# devuelve número a número, no toda la lista a la vez. Muy útil para valores infinitos.
print("Primer número:", next(pares))
# Entra en pausa, podría haber más código entre llamada y llamada
print("Segundo número:", next(pares))
print("Tercer número:", next(pares))

# LISTA SENCILLA SUB ELEMENTOS CON GENERADOR
def generador_ciudades(*ciudades): # * = tupla con número de elementos indefinidos
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento # no hace falta for anidado

ciudades_devueltas = generador_ciudades("Madrid", "Barcelona", "Granada")

# printar letras en ciudades (subelemento de elemento)
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) # se podría hacer con un bucle