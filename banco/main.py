import random
from cliente.Cliente import Cliente
from contas.Contas import ContaCorrente, ContaPoupanca, Banco

#criacao do banco
meu_banco = Banco("Banco Central")
#while true para criacao do menu
while(True):

    print("--------- CAIXA DO BANCO ---------")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar Saldo")
    print("5 - Histórico")
    print("0 - Sair")

    opcao = int(input("Digite sua escolha: "))
    #criacao da caso para manipulacao do menu
    match opcao:
        case 1:
            nome = str(input("Digite seu nome: "))
            cpf = str(input("Digite seu cpf: "))
            endereco = str(input("Digite seu endereco: "))
            numero = random.randint(1000,9999) #criacao do numero da conta aleatoriamente assim que escolhe a opcao
            saldo = 0.0

            novo_cliente = Cliente(nome,cpf,endereco) #criacao do cliente 

            print("---------Escolha entre duas modalidades---------")
            print("1 - CONTA CORRENTE \n 4 saques por mes, livre de taxas apos taxa adicional de R$2,50 por saque \n Limite de cheque especial de ate R$200")
            print("2 - CONTA POUPANCA \n limite de 2 saques por mes sem taxas \n Rende mensalmente 2%")
            op_conta = int(input("Insira o tipo de conta: "))
            #codicional para saber se cliente que cria CC ou CP
            if op_conta == 1:
                nova_conta = ContaCorrente(numero, novo_cliente, saldo)
                meu_banco.adicionar_conta(nova_conta)
                print("Conta criada com sucesso! \nNumero da conta: ",numero)

            elif op_conta == 2:
                nova_conta = ContaPoupanca(numero, novo_cliente, saldo)
                meu_banco.adicionar_conta(nova_conta)
                print("Conta criada com sucesso! \nNumero da conta: ",numero)

            else:
                print("Digite um valor correto!")
        case 2:
            print("\n--------- DEPOSITAR ---------")
            num_busca = int(input("Digite o número da conta: "))
            conta = meu_banco.buscar_conta(num_busca) #chama da fucao depositar
            
            if conta:
                valor_dep = float(input("Digite o valor do DEPÓSITO: "))
                data_op = input("Digite a data (dd/mm/aaaa): ")
                conta.depositar(valor_dep, data_op) #chama da fucao depositar
            else:
                print("Conta não encontrada!") 

        case 3:
            print("\n--------- SACAR ---------")
            num_busca = int(input("Digite o número da conta: "))
            conta = meu_banco.buscar_conta(num_busca) #chama da funcao buscar de banco
            
            if conta:
                valor_saq = float(input("Digite o valor do SAQUE: "))
                data_op = input("Digite a data (dd/mm/aaaa): ")
                conta.sacar(valor_saq, data_op)   #chama da funcao sacar
            else:
                print("Conta não encontrada!")
        case 4:
            print("\n--------- CONSULTAR SALDO ---------")
            num_busca = int(input("Digite o número da conta: "))
            conta = meu_banco.buscar_conta(num_busca)  #chama da funcao buscar
            if conta:
                print(f"Titular: {conta.titular._nome}")
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
            else:
                print("Conta não encontrada!")

        case 5:
            print("\n--------- CONSULTAR HISTÓRICO ---------")
            num_busca = int(input("Digite o número da conta: "))
            conta = meu_banco.buscar_conta(num_busca) #chama da funcao buscar de banco
            if conta:
                print(f"Histórico de {conta.titular._nome}:")
                for op in conta.historico:
                    print(op)
            else:
                print("Conta não encontrada!")
        case 0:
            print("Fechando caixa.......")
            break     
