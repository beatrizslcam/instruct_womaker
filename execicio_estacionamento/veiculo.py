class Veiculo:
    def __init__(self):
        self.placa = ''
        self.estacionado = False
        self.tipo = ''

    def estacionar(self):

        self.estacionado = True

    def sair_da_vaga(self):

        self.estacionado = False