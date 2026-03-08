class Jugador:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    def atacar(self, enemigo, arma):
        print(self.nombre, "ataca a", enemigo.tipo, "con", arma.nombre)
        enemigo.vida -= arma.daño
    def mostrar_estado(self):
        print("jugador:", self.nombre)
        print("vida:", self.vida)

class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

    def mostrar_arma(self):
        print("arma:", self.nombre)
        print("daño:", self.daño)

class Enemigo:
    def __init__(self, tipo, vida, ataque):
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
    def atacar(self, jugador):
        print(self.tipo, "ataca al jugador")
        jugador.vida -= self.ataque
    def mostrar_estado(self):
        print("enemigo:", self.tipo)
        print("vida:", self.vida)
        
arma1 = Arma("Espada Inquisidora", 100)
jugador1 = Jugador("Morgan", 100, 20)
enemigo1 = Enemigo("Lobo infernal", 80, 15)
arma1.mostrar_arma()
jugador1.mostrar_estado()
enemigo1.mostrar_estado()

jugador1.atacar(enemigo1, arma1)

print("después de la pelea:")
jugador1.mostrar_estado()
enemigo1.mostrar_estado()
print("Lobo infernal derrotado")