# Herencias múltiples, uso de super() y isinstance()

class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.residencia)


class Empleado(Persona):
    # se necesita usar el super en el constructor para heredar el de persona
    def __init__(self, nombre, edad, residencia, salario, antiguedad):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()  # se llama a la descripción de persona y se añade al empleado
        print("Salario:", self.salario, "\nAntigüedad:", self.antiguedad)


empleado1 = Empleado("Antonio", 50, "España", 2000, 15)  # en orden del constructor (parámetros)
empleado1.descripcion()

# isinstance() se usa para saber si una instancia pertenece a una clase (true o false):
print(isinstance(empleado1, Empleado))
print(isinstance(empleado1, Persona))
