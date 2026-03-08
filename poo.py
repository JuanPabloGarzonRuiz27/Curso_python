class  jugador:
    def __init__(self, name , gol , trofeos):
        self.name= name
        self.gol= gol
        self.trofeos= trofeos
    def mostrar_goles(self):
        print("Elnombre del jugador es",self.name,)
        print("Numero de goles",self.gol)
        print("Numero de goles",self.trofeos)

jugador1= jugador("Messi",901 ,46)
jugador1.mostrar_goles()