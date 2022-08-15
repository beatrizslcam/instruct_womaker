import veiculo as Veiculo
from estacionamento import Estacionamento
import vaga as Vaga


def menu_estacionar(veiculo):

    placa = input('Digite a placa:')

    match(veiculo):
        case 1:
            carro = Veiculo.Carro()
            carro.placa = input('Digite a placa:')
            vaga = Vaga('carro')
            vaga.ocupar()
            e.estacionar_carro(placa,vaga.id)
            

        case 2:
            moto = Veiculo.Moto()
            moto.placa = input('Digite a placa:')
            vaga = Vaga('moto')
            vaga.ocupar()
            e.estacionar_moto(placa,vaga.id)

        case default:
            print(f'Opção inválida, tente novamente!')

        
def menu_remover(veiculo):

    

    match(veiculo):
        case 1:
            carro = Veiculo.Carro()
            carro.placa = input('Digite a placa:')
            vaga = Vaga('carro')
            vaga.desocupar()
            e.remover_carro(carro.placa,vaga.id)
            

        case 2:
            moto = Veiculo.Moto()
            moto.placa = input('Digite a placa:')
            vaga = Vaga('moto')
            vaga.desocupar()
            e.remover_moto(moto.placa,vaga.id)

        case default:
            print(f'Opção inválida, tente novamente!')          

    


n = True
e = Estacionamento(5,5)

while n:
    acao = input(f'Digite 1 para estacionar ou 2 para remover: ')
    print(acao)
    #if(acao != 1 or acao != 2):
    #    print('Opcao Inválida, tente novamente \n')
        #continue
    
    veiculo = input('Digite 1  para carro ou 2 para moto')
    menu_estacionar(veiculo) 

   # if(acao != 1 or acao != 2):
    #    print('Opcao Inválida, tente novamente')
        #continue
'''if(acao == 1):
        print("entrei")
        menu_estacionar(veiculo) 
        acao = 0

    elif(acao == 2):
        menu_remover(veiculo)
        acao = 0
    '''
    


