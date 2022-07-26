class Carro:
    def __init__(self):
        self.cor = 'Cinza'
        self.ligado = False
        self.modelo = 'G4'
        self.velocidade = 0

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False
        self.velocidade= 0

    def acelera(self):
        if not self.ligado:
            return
        self.velocidade += 10 
  
    def desacelera(self):
        if not self.ligado:
            return
        self.velocidade -= 10 
    
    def __str__(self)-> str:
       return f'Carro - cor {self.cor} - ligado {self.ligado} - modelo {self.modelo} - velocidade {self.velocidade}'



gol = Carro()
gol.liga()

for _ in range(3):
    gol.acelera()

print(f'velocidade do carro {gol.velocidade}')
gol.desliga()
print('velocidade do carro {}'.format(gol.velocidade))