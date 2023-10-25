#DESAFIO1

"""CRIAR UMA CLASSE CARRO QUE TENHA 3 PROPRIEDADES E 3 METODOS"""

class Carro:
    def __init__(self, fabricante, cor, tipo_combustivel):
        self.fabricante = fabricante
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
    
    def Andar(self):
        print("Carro está andando")
    
    def Freiar(self):
        print("Carro precisou freiar")
    
    def Desligar(self):
        print("carro desligado")
    
    def Infocarro(self):
        print(f"carro {self.fabricante} da cor {self.cor} só pode ser usado {self.tipo_combustivel}")

carro1 = Carro("Volkswagem", "Preto", "Gasolina")
carro1.Infocarro()
carro1.Andar()
carro1.Freiar()
carro1.Desligar()