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
from datetime import datetime  

class Cliente:
    def __init__(self,nome, telefone, renda):
        self.id = random_id.uuid4
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda 
        self.__cheque_especial  = 0
class Conta_corrente(Cliente):
    def __init__(self,nome,telefone,renda):
        super().__init__(nome,telefone,renda)
        self.numero_conta = random_id.uuid4
        self.titular = []
        self.__saldo = renda
        self.__operacoes = []
        self.genero= False

    @property
    def get_operacoes(self):
        return self.__operacoes
 
    def set_operacao(self,operacao):
        self.__operacoes = operacao

    def consulta(self):
        print(f'Saldo disponível : {self.__saldo}')

    def lista_operacoes(self,operacao):
        self.__operacoes.append(operacao)

    def saque(self,valor_saque):
        if(valor_saque < self.__saldo):
            self.__saldo = self.__saldo - valor_saque
            self.lista_operacoes({f'Saque: {valor_saque}',datetime.now().strftime('%d/%m/%Y %H:%M')})
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente!')
       
    def deposito(self,valor_deposito):
        self.__saldo = self.__saldo + valor_deposito
        self.lista_operacoes({f'Desposito: {valor_deposito}',datetime.now().strftime('%d/%m/%Y %H:%M')})
        print('Deposito realizado com sucesso!')
    
    def add_titular(self):
        if self.id not in self.titular:
            self.titular.append(self.id)
            print(f'O cliente {self.nome} foi adcionado com sucesso! ')
        else: 
            print(f'O cliente {self.nome}já é títular da conta ')

    def extrato(self):
        print(self.__operacoes)
class Conta_especial(Conta_corrente):
    def __init__(self,nome,telefone,renda):
        super().__init__(nome,telefone,renda)
        self.genero= True
        self.__saldo = renda
        self.__cheque_especial = self.renda_mensal

    def saque(self,valor_saque):
        if(valor_saque < self.__saldo):
            self.__saldo = self.__saldo - valor_saque
            self.lista_operacoes({f'Saque: {valor_saque}',datetime.now().strftime('%d/%m/%Y %H:%M')})
            print('Saque realizado com sucesso!')
        else:
            self.__cheque_especial = valor_saque - self.__cheque_especial
            print('Saque realizado com sucesso!')

    def consulta(self):
        print(f'Saldo disponível : {self.__saldo}, Cheque Especial: {self.__cheque_especial}')

c = Cliente('Maria', '9023234', 3000)
conta = Conta_especial(c.nome, c.telefone, c.renda_mensal)
conta.add_titular()
conta.deposito(10000)
conta.saque(100)
conta.consulta()
conta.extrato()




