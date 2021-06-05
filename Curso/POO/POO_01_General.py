class Coche:
    def __init__(self):  # CONSTRUCTOR
        # Propiedades
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4  # No será accesible desde fuera (encapsulada)
        self.enmarcha = False

    # declarar métodos, funciones especiales de coches (self)
    # Comportamientos
    def arrancar(self, arrancamos):  # a parte de si mismo le pasamos un parámetro
        self.enmarcha = arrancamos
        chequeo = False

        if self.enmarcha:
            chequeo = self.__chequeo_interno()

        if self.enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.enmarcha and chequeo is False:
            return "Algo ha ido mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"

    # muestra el estado del coche
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de",
              self.largoChasis)

    # chequeo antes de arrancar, método encapsulado, no acceder desde fuera
    def __chequeo_interno(self):
        print("Realizando chequeo...")
        self.aceite = "ok"
        self.gasolina = "ok"
        self.puertas = "cerradas"
        if self.aceite == "ok" and self.gasolina == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


print("---------Primer coche---------")
# instanciar coche, crear una instancia, crear un objeto: es lo mismo
coche1 = Coche()
# imprimir propiedades
print(coche1.arrancar(True))
coche1.estado()

print("---------Segundo coche---------")
coche2 = Coche()
print(coche2.arrancar(False))
# coche2.__ruedas = 2 # no queremos que se cambie desde fuera (encapsular con __)
coche2.estado()
