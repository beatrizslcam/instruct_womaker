import veiculo as Veiculo

class Moto(Veiculo):

    def __init__(self,placa):

        super().__init__(self)
        self.placa = placa
        self.tipo = 'Moto'