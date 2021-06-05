email = input("Introduce un email: ")

# correcte si tiene @
for i in email:
    if i == "@":
        print("Correcte")
        break

# No contar el @
counter = 0
for j in email:
    if j == "@":
        continue
    counter += 1

print(counter)

# imprime false o true si hay @
for x in email:
    if x == "@":
        arroba = True
        break
else: # forma parte del for y se ejecuta cuando el bucle esté vacio, si no se usa el break
    arroba = False

print(arroba)