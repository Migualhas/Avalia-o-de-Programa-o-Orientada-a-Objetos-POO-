''' 
Classe operacoes

- Adicionando classe operacoes para manipular e adicionar a historico da conta

'''

class Operacoes:
    def __init__(self, tipo, valor, data):
        self.tipo = tipo
        self.valor = valor
        self.data = data

    def __str__(self):
        return f"{self.data} | {self.tipo}: R$ {self.valor:.2f}"
