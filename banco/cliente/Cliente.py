''' 
Classe Cliente 

- Adicionando classe cliente para usar em conta como atributo

'''


class Cliente:
    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"
