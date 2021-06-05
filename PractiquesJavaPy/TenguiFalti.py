# Primer l'usuari introduirà els cromos repetits. Quan estigui escriurà -1.
# Després l'usuari introduirà els cromos que li falten ordenats de petit a gran. Quan estigui escriurà -1.
# Imprimeix els cromos a canviar


def llista_cromos():
    print("Quan acabis escriu -1")
    cromos = []
    cromo = int(input())
    while cromo != -1:
        cromos.append(cromo)
        cromo = int(input())
    return cromos


def canviar_cromos():
    print("Introdueix llista de cromos repetits:")
    cromos_repetits = llista_cromos()
    print("LLista de cromos repetits: ", cromos_repetits)
    print("Introdueix la llista de cromos que falten:")
    cromos_falten = llista_cromos()
    print("Llista de cromos que falten: ", cromos_falten)
    cromos_canviar = []

    for cromo in cromos_repetits:
        if cromos_falten.__contains__(cromo):
            if not cromos_canviar.__contains__(cromo):
                cromos_canviar.append(cromo)

    print("Cromos a canviar: ", cromos_canviar)


# Main
canviar_cromos()
