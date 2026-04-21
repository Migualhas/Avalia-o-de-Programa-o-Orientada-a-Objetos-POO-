from operacoes.operacoes import Operacoes

''' 
Classe banco

- cria a classe banco para armazenar as contas criadas pelo sistema
- tambem implementa funcoes adicionar e buscar contas 

'''

class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta._numero == numero:
                return conta
        return None

''' 
Classe Conta

- Conta classe Pai 
- Implementa depositar e a propria classe

'''

class Conta:
    def __init__(self, numero, cliente_objeto, saldo):
        self._numero = numero
        self._titular = cliente_objeto  
        self._saldo = saldo
        self._historico = [] 

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor, data):
        if valor <= 0:
            print("Valor inválido")
        else:
            self._saldo += valor
            nova_op = Operacoes("deposito", valor, data)
            self._historico.append(nova_op)
            print(f"Depósito feito com sucesso! Novo saldo: R$ {self._saldo:.2f}")

''' 
Classe ContaCorrente

- ContaCorrente classe filha
- Implementa sacar especifico de CC adicionando a regra de 4 saques por mes sem taxa 
e adicionando taxa de 2.50 apos.
- adiciona atributo limite(Limite especial da conta "Credito")

'''

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)
        self._limite = 200.0

    def sacar(self, valor, data):
        mes_referente = data[2:]
        saq_feito_mes = [
            op for op in self._historico
            if op.tipo == "saque cc" and op.data.endswith(mes_referente)
        ]
        
        total_no_mes = len(saq_feito_mes)
        taxa = 2.50 if total_no_mes >= 4 else 0

        if valor <= 0:
            print("Valor inválido")
        elif (valor + taxa) > (self._saldo + self._limite):
            print("Saldo insuficiente (incluindo limite e taxas)")
        else:
            if taxa > 0:
                print(f"Aviso: Taxa de R$ {taxa:.2f} aplicada pelo excesso de saques.")
            
            self._saldo -= (valor + taxa)
            nova_op = Operacoes("saque cc", valor, data)
            self._historico.append(nova_op)
            print(f"Saque feito com sucesso! Novo saldo: R$ {self._saldo:.2f}")

''' 
Classe ContaPoupanca

- ContaPoupanca classe filha
- Implementa sacar especifico de CP adicionando sacar especifico que apenas permite apenas 2 saques por mes
- Adicionando a regra de juros de rendimento 0.02

'''

class ContaPoupanca(Conta):
    def aplicar_rendimento(self):
        juros = self._saldo * 0.02
        self._saldo += juros
        print(f"Rendimento aplicado: R$ {juros:.2f}. Novo saldo: R$ {self._saldo:.2f}")

    def sacar(self, valor, data):
        mes_referente = data[2:]
        saq_feito_mes = [
            op for op in self._historico
            if op.tipo == "saque cp" and op.data.endswith(mes_referente)
        ]
        
        total_no_mes = len(saq_feito_mes)

        
        if total_no_mes >= 2:
            print(f"Limite atingido! São permitidos apenas 2 saques por mês na Poupança.")
        elif valor <= 0:
            print("Valor inválido")
        elif valor > self._saldo:
            print("Saldo insuficiente (Poupança não possui limite extra)")
        else:
            self._saldo -= valor
            nova_op = Operacoes("saque cp", valor, data)
            self._historico.append(nova_op)
            print(f"Saque feito com sucesso! Novo saldo: R$ {self._saldo:.2f}")
