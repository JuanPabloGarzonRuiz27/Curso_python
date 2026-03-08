class estudiantes:
    def _init_(self, nombre , codigo , promedio):
        self.nombre = nombre
        self.codigo = codigo
        self._promedio = promedio
    def estado(self):
        if self._promedio >= 3.2:
            return("Aprobado")
        else:
            return "Reprobado"
    def informacion(self):
        print(self.nombre,self.estado())
Alumnos = []

e1 = estudiantes("Juan","12345",2.5)
e2 = estudiantes("Carla","12346",3.2)
e3 = estudiantes("Roberta","12347",4.5)

Alumnos.append(e1)
Alumnos.append(e2)
Alumnos.append(e3)
for est in Alumnos:
    est.informacion()
