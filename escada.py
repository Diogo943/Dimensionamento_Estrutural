from math import sqrt, acos, radians, degrees

class Dimensionamento_Escada:
    def __init__(self, e = 0 , H = 0, h = 0, peso_especifico_concreto = 25):
        self.e = e
        self.H = H
        self.h = h
        self.peso_especifico_concreto = peso_especifico_concreto

    def piso(self):
        piso   = 64 - 2 * self.e
        return piso

    def num_degraus(self):
        n_degraus = int(self.H / self.e)

        return n_degraus

    def espelho(self):
        espelho = self.H / self.num_degraus()

        return espelho

    def alhpa(self):
        cos_alhpa = self.piso() / sqrt(self.piso() ** 2 + self.espelho() ** 2)
        alpha = acos(cos_alhpa)

        return degrees(alpha)

    def peso_proprio_patamar(self, hp):
        peso_patamar = hp * self.peso_especifico_concreto

        return peso_patamar

    def espessura_h1(self):
        cos_alhpa = self.piso() / sqrt(self.piso() ** 2 + self.espelho() ** 2)
        h1 = self.h / cos_alhpa

        return h1

    def espessura_h_medio(self):
        espessura_media = self.espessura_h1() + (self.espelho() / 2)

        return espessura_media

    def peso_trecho_inclinado(self):
        peso_trecho = self.peso_especifico_concreto * self.espessura_h_medio()

        return peso_trecho

    def peso_revestimento(self, revestimento = 1):
        return revestimento

    def sobrecarga(self, publico = True):

        if publico:
            sobrecarga = 3
            return sobrecarga
        else:
            sobrecarga = 2.5
            return sobrecarga







dimensionamento_escada = Dimensionamento_Escada(17.5, 150)

piso = dimensionamento_escada.piso()
print(f'Piso: {piso}cm')

n_degraus = dimensionamento_escada.num_degraus()
print(f'Nº degraus: {n_degraus}')

espelho = dimensionamento_escada.espelho()
print(f'Espelho: {espelho}cm')

aplha = dimensionamento_escada.alhpa()
print(f'Alpha: {aplha}º')



