import uuid as random_id

class Veiculo:
    def __init__(self):
        self.placa = ''
        self.estacionado = False
        self.tipo = ''

    def estacionar(self):

        self.estacionado = True

    def sair_da_vaga(self):

        self.estacionado = False

class Carro(Veiculo):

    def __init__(self,placa):

        super().__init__()
        self.placa = placa
        self.tipo = 'Carro'

class Moto(Veiculo):

    def __init__(self,placa):

        super().__init__(self)
        self.placa = placa
        self.tipo = 'Moto'
    
class Vaga:
    def __init__(self):

        self.id = random_id.uuid4()
        self.tipo = ''
        self.placa = ''
        self.livre = True
    
    def ocupar(self):

        self.livre = False
       

    def desocupar(self):

         self.livre = True

    

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

    
            
            


corsa = Carro('ACBDF123')
v = Vaga()
v.ocupar()

gol
corsa.estacionar()
e = Estacionamento(5,5)
n = True
while n:
    veiculo = input('Digite 1  para carro ou 2 para moto')
    switch(veiculo):
        case 1:
            carro = Carro(input('Qual a Placa?'))
            vaga = Vaga()


        case 2:
        
        default:
    n = False



'''

fluxo:
carro()
Vaga()
Estacionamento()

vaga.ocupar()
carro.estacionar()

    
    To do:
    separar as classes
    organizar o menu inicial
    '''