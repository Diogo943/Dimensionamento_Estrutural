#Dimensionamento da Casa Flutuante

class Dimensionamento:
    def __init__(self, pesos = [], volume_concreto = 0.0):
        self.pesos = pesos #kg
        self.volume_concreto = volume_concreto

        #Constantes
        self.DENSIDADE_AGUA = 1000  # kg/m³
        self.GRAVIDADE = 9.81 #m/s²
        self.PESO_ESPECIFICO_AGUA = 10 # KN/m³
        self.PESO_ESPECIFICO_CONCRETO = 25  # kN/m³

    def volume_agua_deslocado(self):

        volume_deslocado = sum(self.pesos) / densidade_agua
        return volume_deslocado

    def empuxo_vertical(self):
        volume_deslocado = self.volume_agua_deslocado()

        empuxo = self.DENSIDADE_AGUA * self.GRAVIDADE * volume_deslocado

    def empuxo_lateral(self):

        ql = hl * self.PESO_ESPECIFICO_AGUA

    def carga_peso(self):
        peso = self.PESO_ESPECIFICO_CONCRETO * self.volume_concreto

        return peso