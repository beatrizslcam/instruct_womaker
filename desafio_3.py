'''# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.
 # 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.
# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".'''
from http import client
import uuid as random_id  

class Cliente:
    def __init__(self,nome, telefone, renda):
        self.id = random_id.uuid4
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda 

class Cliente_Mulher(Cliente):
    def __init__(self,nome, telefone, renda):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda 
         self.__cheque_especial 


      
    def valor_cheque(self):
        self.__cheque_especial = True


class Conta_corrente:
    def __init__(self):
        self.numero_conta = random_id.uuid4
        self.titular = []
        self.__saldo = 0
        self.__operacoes = []
       
    

    # colocar os getters e setters

  

    def consulta(self):
        print(f'Saldo disponível : {self.__saldo}')

    def operacoes(self,operacao):
        self.__operacoes.append(operacao)

    def saque(self,valor_saque):
        self.__saldo = self.__saldo - valor_saque
        operacoes('saque')
        print('Saque realizado com sucesso!')
    
    
    def deposito(self,valor_deposito):
        self.__saldo = self.__saldo + valor_deposito
        operacoes('deposito')
        print('Deposito realizado com sucesso!')
    
    def add_titular(self, cliente : Cliente):
        if cliente.id not in self.titular:
            self.titular.append(cliente.id)
        else: 
            print(f'O cliente {cliente.nome}já é títular da conta ')
    



