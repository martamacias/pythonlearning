# Marta Macias Gordon
# 20/03/2021
# diccionari = {'id':123, 'nom':'Joan'}
# diccionari['id'] = 345


def exemple_clear():
    print('Mètode clear per buidar un diccionari: ')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari actual: ', diccionari)
    # Fem el clear
    diccionari.clear()
    print('Diccionari buit: ', diccionari)
    input('Enter per continuar... \n')


def exemple_copy():
    print('Mètode copy per copiar un diccionari: ')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari actual:', diccionari)
    # Copiem el diccionari
    diccionari2 = diccionari.copy()
    print('Diccionari copiat:', diccionari2)
    input('Enter per continuar...\n')


def exemple_fromkeys():
    print('Mètode fromkeys per crear un diccionari a partir de uns valor donats: ')
    # definir els valors
    keys = ('key1', 'key2', 'key3')
    values = 1, 2, 3
    # crear el diccionari
    diccionari = dict.fromkeys(keys, values)
    print('keys: ', keys)
    print('valors: ', values)
    print('Diccionari: ', diccionari)
    input('Enter per continuar...\n')


def exemple_values():
    print('Mètode values per recuperar valors de un diccionari: ')
    diccionari = {'id': 123, 'nom': 'Joan'}
    # recuperar valors
    values = diccionari.values()
    print('Diccionari: ', diccionari)
    print('Valors extrets: ', values)
    input('Enter per continuar...\n')


def exemple_keys():
    print('Mètode keys per recuperar claus de un diccionari: ')
    diccionari = {'id': 123, 'nom': 'Joan'}
    # recuperar claus
    keys = diccionari.keys()
    print('Diccionari: ', diccionari)
    print('Valors extrets: ', keys)
    input('Enter per continuar...\n')


def exemple_get():
    print('Mètode get per recuperar el valor de una clau: ')
    diccionari = {'id': 123, 'nom': 'Joan'}
    # recuperar valor
    value = diccionari.get('id')
    print('Diccionari: ', diccionari)
    print('Valor de id: ', value)
    input('Enter per continuar...\n')


def exemple_pop():
    print('Mètode pop per eliminar un element del diccionari posant la clau:')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari original: ', diccionari)
    # Eliminar el id
    diccionari.pop('id')
    print('Diccionari sense el id: ', diccionari)
    input('Enter per continuar...\n')


def exemple_items():
    print('Mètode items per mostrar els items del diccionari:')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari: ', diccionari)
    items = diccionari.items()
    print('Items: ', items)
    input('Enter per continuar...\n')


def exemple_popitem():
    print('Mètode popitem per eliminar el últim item del diccionari:')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari: ', diccionari)
    diccionari.popitem()
    print('Diccionari sense el nom', diccionari)
    input('Enter per continuar...\n')


def exemple_setdefault():
    print('Mètode setdefault per retornar el valor de una clau del diccionari:')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari: ', diccionari)
    value = diccionari.setdefault('id')
    print('Valor de id: ', value)
    input('Enter per continuar...\n')


def exemple_update():
    print('Mètode update per afegir valors nous, i si la clau no existeix fa un update del diccionari:')
    diccionari = {'id': 123, 'nom': 'Joan'}
    print('Diccionari: ', diccionari)
    # Canviar el id a 152
    diccionari.update({'id': 152})
    print('Diccionari amb valor nou de id: ', diccionari)
    input('Enter per continuar...\n')


def exemples_diccionari():
    exemple_clear()
    exemple_copy()
    exemple_fromkeys()
    exemple_values()
    exemple_keys()
    exemple_get()
    exemple_pop()
    exemple_items()
    exemple_popitem()
    exemple_setdefault()
    exemple_update()


# main
exemples_diccionari()
