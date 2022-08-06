import veiculo as Veiculo

class Carro(Veiculo):

    def __init__(self,placa):

        super().__init__()
        self.placa = placa
        self.tipo = 'Carro'