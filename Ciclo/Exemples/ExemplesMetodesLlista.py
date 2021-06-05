# Marta Macias Gordon
# 07/03/2021


# Mètode append que afegeix un element al final de la llista
def exemple_append():
    print("Mètide append per afegir un element al final de la llista:")
    llista = [1, 2, 3]
    # Printar llista abans de fer l'append
    print(llista)
    llista.append(4)
    # Printar llista amb l'element afegit
    print(llista)
    input("Prem enter per continuar...")


# Mètode clear per deixar la llista buida
def exemple_clear():
    print("Mètode clear per deixar la llista buida:")
    llista = [1, 2, 3, 4]
    # Printar la llista
    print(llista)
    llista.clear()
    # Printar la llista buida
    print(llista)
    input("Prem enter per continuar...")


# Mètode copy per copiar una llista
def exemple_copy():
    print("Mètode copy per copiar una llista:")
    llista = [1, 2, 3, 4]
    # Printar la llista original
    print("Llista original: ", llista)
    llista_copy = llista.copy()
    # Printar la llista copiada
    print("Llista copiada: ", llista_copy)
    input("Prem enter per continuar...")


# Mètode count per comptar les vegades que surt un element a la llista
def exemple_count():
    print("Mètode count per comptar les vegades que surt un element a la llista:")
    llista = [1, 2, 3, 3]
    # Printar la llista
    print(llista)
    llista.count(3)
    # Printar els cops que surt el 3
    value = llista.count(3)
    print("Vegades que surt el 3: ", value)
    input("Prem enter per continuar...")


# Mètode extend per afegir elements a la llista
# També es pot fer amb un +
def exemple_extend():
    print("Mètode extend per afegir elements (altre llista) a la llista:")
    llista = [1, 2, 3]
    # Printar la llista
    print(llista)
    # Crear una altre llista i printar-la
    elements = [4, 5, 6]
    print(elements)
    llista.extend(elements)
    # Printar llista final
    print("Llista finlal: ", llista)
    input("Prem enter per continuar...")


# Mètode sort per ordenar una llista
def exemple_sort():
    print("Mètode sort per ordenar una llista modificant-la:")
    llista = [2, 4, 1, 3, 8]
    print("Llista original: ", llista)
    # Llista sense reverse
    llista.sort(reverse=False)
    print("Llista amb reverse False: ", llista)
    # Llista amb reverse
    llista.sort(reverse=True)
    print("Llista amb reverse True: ", llista)
    input("Prem enter per continuar...")


# Mètode sort per ordenar una llista creant una nova
# Només ordena llistes amb el mateix tipus de variable (no lletres i números)
def exemple_sorted():
    print("Mètode sort per ordenar una llista creant una nova:")
    llista = [2, 4, 1, 3, 8]
    print("Llista original: ", llista)
    # Llista ordenada
    llista2 = sorted(llista)
    print("Llista ordenada: ", llista2)
    input("Prem enter per continuar...")


# Mètode per insertar un valor a la llista en la posició que volem
def exemple_insert():
    print("Mètode per insertar un valor a la llista en la posició que volem:")
    llista = [1, 2, 3, 4]
    print("Llista original: ", llista)
    # Afegir un valor (posició, valor)
    llista.insert(0, 6)
    print("Llista amb el volor nou: ", llista)
    input("Prem enter per continuar...")


# Mètode per revertir una llista
def exemple_reverse():
    print("Mètode per revertir una llista:")
    llista = [1, 2, 3, 4]
    print("Llista original: ", llista)
    # Revertir la llista
    llista.reverse()
    print("Llista revertida: ", llista)
    input("Prem enter per continuar...")


# Mètode pop per eliminar un element de la llista per index
def exemple_pop():
    print("Mètode pop per eliminar un element de la llista posant el seu index:")
    llista = [1, 2, 3, 4]
    print("Llista original: ", llista)
    # Eliminar l'element (posició)
    llista.pop(2)
    print("Llista amb el valor eliminat: ", llista)
    input("Prem enter per continuar...")


# Mètode que retorna el primer índex d'un valor donat
def exemple_index():
    print("Mètode que retorna el primer índex d'un valor donat:")
    llista = [1, 2, 3, 4]
    print("Llista: ", llista)
    # Buscar l'índex
    index = llista.index(3)
    print("El 3 està a la posició: ", index)
    input("Prem enter per continuar...")


# Mètode per eliminar un element de la llista passat per paràmentre
def exemple_remove():
    print("Mètode remove per eliminar un element de la llista passat per paràmentre")
    llista = [1, 2, 3, 4]
    print("Llista: ", llista)
    # Eliminar l'element (element)
    llista.remove(3)
    print("LLista després del remove: ", llista)
    input("Prem enter per continuar...")


def exemples_llista():
    exemple_append()
    exemple_clear()
    exemple_copy()
    exemple_count()
    exemple_extend()
    exemple_sort()
    exemple_sorted()
    exemple_insert()
    exemple_reverse()
    exemple_pop()
    exemple_index()
    exemple_remove()


# main
exemples_llista()
