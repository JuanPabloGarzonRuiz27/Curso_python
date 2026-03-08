# clase libro ,titulo ,autor , año,2 instancias de libro  y imprimir el titulo en la terminal
class libros:
    def __init__(self , titulo , autor , año ):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        print("tenemos estos libros:""", titulo , autor , año)
libro1 = libros("Dejad que los niños vengan a mí","De Juan Pablo Barrientos",2019)
libro2 = libros("narraciones extraordinarias","De Edgar Allan Poe",2024)
