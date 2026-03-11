class Vehiculo:
    def __init__(self, marca, modelo, linea, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.linea = linea
        self.__velocidad = velocidad

    def aceleracion(self):
        self.__velocidad += 1

    def mostrar_info(self):
        print("informacion del vehículo:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Línea: {self.linea}")
        print(f"  Velocidad: {self.__velocidad}")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, linea, num_puertas):
        super().__init__(marca, modelo, linea)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"  numero de puertas: {self.num_puertas}")
        print(" carro")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, linea, cilindrada):
        super().__init__(marca, modelo, linea)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"  Cilindraje: {self.cilindrada} cc")
        print(" moto")

vehiculos = []

carro1 = Carro("FORD", "Ranger", "2024", 4)
carro2 = Carro("TOYOTA", "Land Cruiser Prado", "2023", 5)
carro3 = Carro("RENAULT", "Oroch", "2024", 4)
moto1 = Moto("PULSAR", "N125", "2022", 125)
moto2 = Moto("YAMAHA", "XTZ 150", "2023", 150)
moto3 = Moto("KTM", "Duke 250", "2023", 250)

vehiculos.append(carro1)
vehiculos.append(carro2)
vehiculos.append(carro3)
vehiculos.append(moto1)
vehiculos.append(moto2)
vehiculos.append(moto3)

for transporte in vehiculos:
    transporte.mostrar_info()
    print("_"*20)
