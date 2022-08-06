class Estacionamento:
    def __init__(self, numero_vaga_carro, numero_vaga_moto):

        self.vagas_de_carro = numero_vaga_carro
        self.vaga_de_moto = numero_vaga_moto
        self.carro_para_vaga  = []
        self.moto_para_vaga = []
        self.total_vagas_livres_carro = numero_vaga_carro
        self.total_vags_livres_moto = numero_vaga_moto

    def estacionar_carro(self,placa_carro,vaga_id):

        if(self.total_vagas_livres_carro > 0):

            self.carro_para_vaga.append({vaga_id, placa_carro})
            self.total_vagas_livres_carro -= 1
            
            print(f'Carro de placa {placa_carro} estacionado com sucesso na vaga {vaga_id}!')

        else:
            print("Estacionamento de Carro Lotado!")
        
    
    def estacionar_moto(self,placa_moto,vaga_id):

        if(self.total_vagas_livres_moto > 0):

            self.carro_para_vaga.append({vaga_id, placa_moto})
            self.total_vagas_livres_carro -= 1
            
            print(f'Moto de placa {placa_moto} estacionado com sucesso na vaga {vaga_id}!')

        else:
            print("Estacionamento de moto lotado!")
        

    def remover_carro(self,placa_carro,vaga_id):
        self.carro_para_vaga.remove({vaga_id, placa_carro})
        self.total_de_vagas_livres_carro +=1


    def remover_moto(self,placa_moto,vaga_id):

        self.moto_para_vaga.remove({vaga_id, placa_moto})
        self.total_de_vagas_livres_moto +=1

    def estado_estacionamento(self):
        if(self.total_vagas_livres_carro >0): 

            print(f'Vagas para carro disponíveis: {self.total_vagas_livres_carro}')
        else:
            print("Estacionamento de carro lotado!")


        if(self.total_vagas_livres_moto >0): 

            print(f'Vagas para moto disponíveis: {self.total_vagas_livres_moto}')
        else:
            print("Estacionamento de carro lotado!")
