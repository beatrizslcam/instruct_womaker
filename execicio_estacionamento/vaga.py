import uuid as random_id  
class Vaga:
    def __init__(self,tipo):

        self.id = random_id.uuid4()
        self.tipo = tipo
        self.livre = True
    
    def ocupar(self):

        self.livre = False
       

    def desocupar(self):

         self.livre = True