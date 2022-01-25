# Declaramos la clase y sus métodos
class Enfrentamiento:
    def __init__(self, comp1='', comp2='', punt1=0, punt2=0):
        self.competidor1 = comp1
        self.competidor2 = comp2
        self.puntos1 = punt1
        self.puntos2 = punt2

    # devuelve el Competidor que gana el enfrentamiento
    def ganador(self):
        if self.puntos1 > self.puntos2:
            return self.competidor1
        else:
            return self.competidor2

    # devuelve el Competidor que pierde el enfrentamiento
    def perdedor(self):
        if self.puntos1 < self.puntos2:
            return self.competidor1
        else:
            return self.competidor2


    def fixture(self):
        f = ''
        f += '{:>20}'.format(self.competidor1.nombre)
        f += '{:^40}'.format('vs.')
        f += '{:<20}'.format(self.competidor2.nombre)
        return f

    def to_string(self):
        s = ''
        s += '{:<15}'.format(self.competidor1.nombre)
        s += '{:>15}'.format(str(self.puntos1))
        s += '{:^20}'.format('vs.')
        s += '{:<15}'.format(str(self.puntos2))
        s += '{:>15}'.format(self.competidor2.nombre)
        s += '\n\n'
        s += '{:^80}'.format('El ganador es: ' + self.ganador().nombre)

        return s
