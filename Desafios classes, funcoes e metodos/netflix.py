class Netflix:
    #método com parametros inicias e se o plano não estiver na lista de "listas planos" ele vai exibir um erro
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.lista_planos = ["basic", "premium"]
        if plano not in self.lista_planos:
            print("você não possui um plano valido")
        else:
            print(f"bem vindo {nome}")
        
#metodo com função de mudar o plano 
    def mudar_plano(self, novo_plano):
            if novo_plano in self.lista_planos:
             self.plano = novo_plano
            else:
                print("plano invalido")

# metodo com função de assistir o filme conforme o plano.
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"ver filme {filme}")
        elif self.plano == "premium":
            print(f"ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print(f"faça o upgrade para assistir o {filme}")
        else:
            print("plano invalido")
        



cliente1 = Netflix("Michael", "michaelsergio02@gmail.com", "basic")
print(cliente1.plano)
cliente1.ver_filme("As branquelas", "premium")
cliente1.mudar_plano("premium")
print(cliente1.plano)
cliente1.ver_filme("As branquelas", "premium")