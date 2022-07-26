# Definição da classe

class Televisao:

    def __init__(self):
        self.ligada = False 
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada= True

    def desligar(self):
        self.ligada= False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        if self.canal< self.canal_max:
            self.canal +=1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        if self.canal> self.canal_min:
            self.canal -=1
    
    def aumentar_volume(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 10 
    
    def reduzir_volume(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume += 10 

    def mudo(self):
        if not self.ligada:
            return
        self.volume = 0

    def retirar_mudo(self):
        if not self.ligada:
            return
        self.volume = 30

    def __str__(self)-> str:
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'



#criando instâncias da class Televisão
tv_sala = Televisao()
tv_quarto = Televisao()



tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada))

for _ in range(3):
    tv_sala.aumentar_volume()

print(f'tv_sala volume: {tv_sala}') #mostra toda a instância
print(f'tv_quarto volume: {tv_quarto.volume}')