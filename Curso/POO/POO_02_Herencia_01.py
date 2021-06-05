class Vehiculo:  # clase padre
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
              "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)


class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculo):  # clase moto a partir de clase vehiculo
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Haciendo el caballito"

    def estado(self):  # se sobreescribe el método de vehículo añadindo métodos de moto
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
              "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n" + self.hcaballito)


class VElectricos:
    def __init__(self):
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True


# creando instancias
print("--------Moto-------")
moto1 = Moto("Honda", "CBR")
moto1.caballito()  # activa caballito
moto1.estado()

print("--------Furgoneta-------")
furgoneta1 = Furgoneta("Renault", "Kangoo")
furgoneta1.arrancar()
print(furgoneta1.carga(True))
furgoneta1.estado()


# Herencia múltiple
# se da prioridad al constructor (__init__) y métodos de la primera clase que se escribe (VElectricos)
class BicicletaElectrica(VElectricos, Vehiculo):
    pass


bici1 = BicicletaElectrica()  # no se pone nada por el __init__ de VElectricos
# ver más del constructor y super() en el POO_03
