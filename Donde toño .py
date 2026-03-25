class Producto:
    def __init__(self, nombre, precio, categoria, prioridad):
        self.nombre = str(nombre)
        self.precio = float(precio)
        self.categoria = str(categoria)
        self.prioridad = prioridad

    def mostrar(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio}"

class Pedido:
    def __init__(self, mesa, producto, cantidad, precio, prioridad):
        self.mesa = mesa
        self.producto = producto
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio)
        self.prioridad = prioridad

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def ticket_caja(self):
        total = self.calcular_total()
        print(f"--- TICKET CAJA --- \nProducto: {self.producto} x{self.cantidad} | Total: ${total}")


def menu_principal():
    print("\n--- BIENVENIDO AL RESTAURANTE ---")
    print("1. Agregar pedido")
    print("2. Procesar pedido de cocina (Siguiente en cola)")
    print("3. Ver cola de cocina (Por prioridad)")
    print("4. Ver cuenta de la mesa")
    print("5. Pagar cuenta de la mesa")
    print("6. Salir")

def menu_de_comida():
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Bandeja paisa --- $25000")
    print("2. Lechona  ----------- $30000")
    print("3. sancocho -------- $20000")
    print("4. Helado de mora ------------ $2000")
    print("5. Ensalada de frutas con helado -- $25000")
    print("6. Volver al menú")

def sistema_de_heladeria():
    productos_menu = {
        "1": {"nombre": "Bandeja paisa", "precio": 25000, "categoria": "comida", "prioridad": 3},
        "2": {"nombre": "Lechona",           "precio": 30000, "categoria": "comida", "prioridad": 2},
        "3": {"nombre": "Sancocho",        "precio": 2500, "categoria": "comida", "prioridad": 3},
        "4": {"nombre": "Helado de mora",            "precio": 2000, "categoria": "bebida", "prioridad": 1},
        "5": {"nombre": "Ensalada de frutas con helado", "precio": 25000, "categoria": "bebida", "prioridad": 1}
    }
    
    heladeria = []

    while True:
        menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_de_comida()
            prod_opc = input("Dígito del producto: ")
            
            if prod_opc == "6": continue
            
            if prod_opc in productos_menu:
                datos = productos_menu[prod_opc]
              
                prod_obj = Producto(datos["nombre"], datos["precio"], datos["categoria"], datos["prioridad"])
                
                mesa = input("Número de mesa: ")
                cant = int(input("Cantidad: "))
                
                
                nuevo_pedido = Pedido(mesa, prod_obj.nombre, cant, prod_obj.precio, prod_obj.prioridad)
                heladeria.append(nuevo_pedido)
                print(f"Agregado: {nuevo_pedido.producto} para Mesa {nuevo_pedido.mesa}")
            else:
                print("Opción no válida.")

        elif opcion == "2":
            if not heladeria:
                print("No hay pedidos pendientes.")
            else:
                
                atendido = heladeria.pop(0)
                print(f"Cocinando: {atendido.producto} para Mesa {atendido.mesa}")

        elif opcion == "3":
            if not heladeria:
                print("Cola vacía.")
            else:
                
                cola_ordenada = sorted(heladeria, key=lambda x: x.prioridad, reverse=True)
                print("\n--- COLA POR PRIORIDAD ---")
                for p in cola_ordenada:
                    print(f"Prio: {p.prioridad} | Mesa {p.mesa}: {p.producto} x{p.cantidad}")

        elif opcion == "4" or opcion == "5":
            mesa_buscada = input("Número de mesa: ")
            pedidos_mesa = [p for p in heladeria if p.mesa == mesa_buscada]
            
            if not pedidos_mesa:
                print(f"La Mesa {mesa_buscada} no tiene pedidos.")
                continue
                
            total = sum(p.calcular_total() for p in pedidos_mesa)
            print(f"\n--- CUENTA MESA {mesa_buscada} ---")
            for p in pedidos_mesa:
                print(f"{p.producto} x{p.cantidad}: ${p.calcular_total()}")
            print(f"TOTAL: ${total}")

            if opcion == "5":
                
                heladeria = [p for p in heladeria if p.mesa != mesa_buscada]
                print(f"Mesa {mesa_buscada} pagada y liberada.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    sistema_de_heladeria()