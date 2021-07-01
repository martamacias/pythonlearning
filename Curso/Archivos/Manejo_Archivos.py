from io import open

def escribir():
    # abrir archivo modo write
    archivo_texo=open("Curso/Archivos/archivo.txt","w")
    # crear frase
    frase="Frase de prueba para escribir en el archivo.\nHoy es jueves.\n"
    #escribir en el archivo
    archivo_texo.write(frase)
    #cerrar archivo
    archivo_texo.close()

def leer():
    # abrir archivo modo read
    archivo_texo=open("Curso/Archivos/archivo.txt","r")
    # leer archivo + almacenar info
    texto=archivo_texo.read()
    # cerrar archivo
    archivo_texo.close()
    # mostrar info por terminal
    print(texto)
    # APUNTE: opción read(N caracter limite de lectura), y el puntero se queda ahí

def leer_lineas():
    # abrir archivo modo read
    archivo_texo=open("Curso/Archivos/archivo.txt","r")
    # leer lineas archivo + almacenar info en lista iterable
    lineas_texto=archivo_texo.readlines()
    # cerrar archivo
    archivo_texo.close()
    # mostrar info por terminal
    print(lineas_texto)

def agregar_lineas():
    # abrir archivo modo append
    archivo_texo=open("Curso/Archivos/archivo.txt","a")
    # crear frase
    frase="Frase modo append que se añade al final.\n"
    #escribir en el archivo
    archivo_texo.write(frase)
    #cerrar archivo
    archivo_texo.close()

def situar_puntero():
    # abrir archivo modo read
    archivo_texo=open("Curso/Archivos/archivo.txt","r")
    # mostrar info por terminal
    print(archivo_texo.read())
    # situar el puntero desde N caracteres
    archivo_texo.seek(5)
    # mostrar info por terminal
    print(archivo_texo.read())
    #cerrar archivo
    archivo_texo.close()

def lectura_escritura():
    escribir()
    agregar_lineas()
    # abrir archivo modo read + write
    archivo_texo=open("Curso/Archivos/archivo.txt","r+")
    # leer archivo
    print("Lineas antes:\n"+archivo_texo.read())
    # situar puntero al principio
    archivo_texo.seek(0)
    # almacenar lineas en lista
    lines=archivo_texo.readlines()
    # cambiar línea de la lista
    lines[1]="Linea añadida en el método lectura_escritura\n"
    archivo_texo.seek(0)
    # escribir lineas lista
    archivo_texo.writelines(lines)
    archivo_texo.seek(0)
    # leer archivo
    print("Lineas después:\n"+archivo_texo.read())
    # cerrar archivo
    archivo_texo.close()

#escribir()
#leer()
#leer_lineas()
#agregar_lineas()
#situar_puntero()
lectura_escritura() 