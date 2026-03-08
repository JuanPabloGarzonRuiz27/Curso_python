# class Estudiante:
#     def _init_(self, nombre , codigo , promedio):
#     self.nombre = nombre
#     self.codigo = codigo
#     self.promedio = promedio
marca  = input("ingresa la marca del automovil:""")
modelo = input("ingresa el modelo del automovil:""")
class carros:
    def __init__(self, marca , modelo):
        self.marca = marca
        self.modelo = modelo
        print("Tenemos estos modelos disponibles:"" ", marca , modelo)
car1 = carros("TWINGO", 2000 )
print(car1.marca)
print(car1.modelo)
