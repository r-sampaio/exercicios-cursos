# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = input(str('Nova cor: '))
        return self.cor

    def mostraCor(self):
        return self.cor

bola = Bola('Verde', 20, 'plastico')
bola.trocaCor()
print(bola.cor, bola.circunferencia, bola.material)
