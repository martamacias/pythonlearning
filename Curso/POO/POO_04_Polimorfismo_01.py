class Coche:
    def desplazamiento(self):
        print("Me desplazo sobre 4 ruedas.")


class Moto:
    def desplazamiento(self):
        print("De desplazo sobre 2 ruedas.")


class Camion:
    def desplazamiento(self):
        print("Me desplazo dobre 6 ruedas.")


# con esta función se puede cambiar el tipo de vehículo
def desplazamiento_vehiculo(vehiculo):  # en java se tiene que especificar poniendo object o por herencia
    vehiculo.desplazamiento(vehiculo)


# desplazamiento según el vehículo que se pase por parámetro
vehiculo1 = Coche
desplazamiento_vehiculo(vehiculo1)
