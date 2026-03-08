class producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_stock(self, cantidad):
        self.cantidad_disponible += cantidad

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: {self.precio} - Stock: {self.cantidad_disponible}")

class cliente:
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} - ID: {self.ID}")

class venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        self.lista_productos.append((producto, cantidad))
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(producto.precio * cantidad for producto, cantidad in self.lista_productos)

    def mostrar_venta(self):
        print(f"Venta para el cliente: {self.cliente.nombre}")
        for producto, cantidad in self.lista_productos:
            print(f"- {producto.nombre}: {cantidad} x {producto.precio} = {producto.precio * cantidad}")
        print(f"Total: {self.total}")

# Crear productos
producto1 = producto("Manzana", 1.0, 50)
producto2 = producto("Pan", 0.5, 100)

# Crear cliente
cliente1 = cliente("Laura", "12345")
cliente2=cliente("Oscar","13470")

# Crear venta
venta1 = venta(cliente1)
venta2=venta(cliente2)

# Agregar productos a la venta
venta1.agregar_producto(producto1, 5)
venta1.agregar_producto(producto2, 10)
venta2.agregar_producto(producto1,2)

# Mostrar la venta
venta1.mostrar_venta()
venta2.mostrar_venta()