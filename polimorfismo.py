class animal:
    def sonidos(self):
        pass
class vaca(animal):
    def sonidos(self):
        print("Muuuu",)
class cerdo(animal):
    def sonidos(self):
        print("Oiiin",)
class gallo(animal):
    def sonidos(self):
        print("kikiriki",)
animales=[vaca(),
          cerdo(),
          gallo()]
for animal in animales:
    animal.sonidos()

