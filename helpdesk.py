class Ticket:
    def __init__(self,asunto, prioridad):
        self.asunto=asunto
        self.prioridad=prioridad
        self.__estado="abierto"
    def ver_estado(self):
        return self.__estado
    def cambiar_estado(self,nuevo_estado):
        validados=("abierto","en_tramite","cerrado")
        if nuevo_estado in validados:
            self.__estado=nuevo_estado
        else:
            print("Error de estado y no es valido") 
    def verificar(self):
        return"Resolucion generica del ticket"
    
class ticket_software(Ticket):
    def verificar(self):
        return"Revisar software"
    
class ticket_hardware(Ticket):
    def verificar(self):
        return"Revisar hardware"
    
class ticket_red(Ticket):
    def verificar(self):
        return"Revisar la red"
#menu
def mostrar_menu():
    print("###### welcome to the ticket#####")
    print("1. Craer ticket")
    print("2. Cambiar ticket")
    print("3. Resumen de los tickets")
    print("4. Salir")
def  menu_del_ticket():
    tipo=input("selecciona el tipo:")
    asunto=input("ingrese el asunto:")
    prioridad=input("ingresa la prioridad(Alta,Media,Baja)")
    if tipo == "1":
       return ticket_software(asunto,prioridad)
    elif tipo == "2":
        return ticket_hardware(asunto,prioridad)
    elif tipo == "3":
        return ticket_red(asunto,prioridad)
    else:
        print(" tipo de ticket no valido")
        return None
Tickets=[]

while True:
    mostrar_menu()
    op = input("elige la opcion que deseas")
    if op =="1":
        Tickets= menu_del_ticket
#     print("1.Crear Ticket 2.cambiar estado 3.Resumen de Ticket 4.salir")
#     opcion=input("Escoge que opcion del menu")
#     if opcion == "1":
#         Tickets.append(Ticket)
#     elif opcion == "2":
#         print("Ticket no registrado")
#         Tickets.append()





   

