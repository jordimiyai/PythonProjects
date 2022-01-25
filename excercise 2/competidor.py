# Declaramo la clase y su método
class Competidor:
    def __init__(self, nom='', cont=0, rank=0):
        self.nombre = nom
        self.continente = cont
        self.ranking = rank

    def to_string(self):
        cont = ('América', 'Europa', 'Asia', 'África', 'Oceanía')
        c = ''
        c += '{:<25}'.format('Nombre: ' + self.nombre)
        c += '{:<30}'.format('Continente: ' + '[' + str(self.continente) + '] ' + str(cont[self.continente]))
        c += '{:<15}'.format('Ranking: ')
        c += '{:>10}'.format(str(self.ranking))

        return c
