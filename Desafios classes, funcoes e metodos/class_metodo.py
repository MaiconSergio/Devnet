class Computador:
    def __init__(self, marca, memoria_ram, placa_de_vide):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa = placa_de_vide
    
    def Ligar(self):
        print("Estou ligando")
    
    def Desligar(self):
        print("estou desligando")

    def Exibirinfo(self):
        print(self.marca, self.memoria_ram, self.placa)
    

computador1 = Computador("Asus", "8gb", "Nvidia")
computador1.Ligar()
computador1.Desligar()
computador1.Exibirinfo()