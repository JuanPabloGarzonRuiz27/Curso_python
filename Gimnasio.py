# Grupo C
# Danna Ximena Bañol Cañas
# Juan Pablo Garzon Ruiz
# Dorat Oriana Mejias Valero

class requerimientos:
    def __init__(self,nombre, edad, tipo_membresia):
        self.nombre=nombre
        self.edad=edad
        self.__estado= "inactivo" 
        self._tipo_membresia= tipo_membresia

    def mostrar_estado(self):
        return self.__estado
    
    def cambiar_estado (self, nuevo_estado):
        membresia_opciones=["activo", "inactivo"]
        if nuevo_estado in membresia_opciones:
            self.__estado = nuevo_estado
        else:
            print("estado invalido")

    def acceso(self):
        if self.__estado == "activo":
            print("acceso consedido")
        else:
            print("acceso no consedido")
    
    def resumen(self):
        return f"nombre: {self.nombre}, edad: {self.edad}, tipo de membresia: {self._tipo_membresia}, estado: {self.__estado}"

#menu

def mostrar_menu():
    print("#####Bienvenido al gimnasio#####")
    print("1.Crear membresia")
    print("2. cambiar estado")
    print("3. Resumen de tu membresia") 
    print("4;salir")

def estado_de_la_membresia():
    print("##### Escoge el tipo de membresia#####")
    print("1. quincenal")
    print("2. mensual")
    print("3. trimestral") 
    print("4,salir")

    estado=input ("elige el tipo de membresia: ")
    nombre=input ("ingresa tu nombre: ")
    edad=input("ingresa tu edad: ")

    if estado =="1":
        return requerimientos (nombre, edad,"quincenal")
    elif estado =="2":
        return requerimientos (nombre, edad, "mensual")
    elif estado =="3":
        return requerimientos (nombre, edad, "trimestral")
    else:
        print("invalido")
        return None

membresia = [] 
while True:
    mostrar_menu ()
    opcion=input("elige una opción: ") 
    if opcion == "1":
        mem = estado_de_la_membresia()
        if mem is not None:
            membresia.append(mem)

    elif opcion == "2":
        nombre_buscar = input("ingresa el nombre de la membresia que deseas cambiar el estado: ")
        nuevo_estado = input("ingresa el nuevo estado (activo/inactivo): ")
        
        for m in membresia:
            if m.nombre == nombre_buscar:
                m.cambiar_estado(nuevo_estado)
                print("estado cambiado exitosamente")
                break
        else:
            print("membresia no encontrada")

    elif opcion == "3":
        print("resumen de todas las membresias")
        for m in membresia:
            print(m.resumen())

    elif opcion == "4":
        print("gracias por usar el sistema de membresias del gimnasio")
        break
    else:
        print("opcion no valida")




    
