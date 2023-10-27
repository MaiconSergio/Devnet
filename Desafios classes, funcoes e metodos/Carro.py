#DESAFIO1

"""CRIAR UMA CLASSE CARRO QUE TENHA 3 PROPRIEDADES E 3 METODOS"""
#classe criada com o nome de carro e seus parametros (caracteristicas)
class Carro:
    def __init__(self, fabricante, cor, tipo_combustivel):
        self.fabricante = fabricante
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.status = "Desligado"
    
    # um método criado com a a função de "andar" então ele se o status estiver "desligado"
    #o status fica automaticamente "Ligado" e começa a andar e caso ao contrário e necessário ligar.
    def Andar(self, status):
        self.status = status
        if self.status == "Ligado":
            print(f"O carro está {self.status}")
        else:
            print("necessário ligar o carro")
        
        # outro método que possui a função de "Freiar"
    def Freiar(self):
        if self.status == "Ligado":
           print("Carro precisou freiar para não gerar acidente")
    
    #método de desligar o carro
    def Desligar(self):
        if self.status == "Ligado":
           self.status = "Desligado"
           print("carro desligando")
   
    # método com informações do carro a serem exibidas 
    def Infocarro(self):
        print(f"carro {self.fabricante} da cor {self.cor} só pode ser usado {self.tipo_combustivel}")

carro1 = Carro("Volkswagem", "Preto", "Gasolina")
carro1.Infocarro()
carro1.Andar("Ligado")
carro1.Freiar()
carro1.Desligar()

