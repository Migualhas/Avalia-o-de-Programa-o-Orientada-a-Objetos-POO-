# Sistema de Caixa Eletrônico (ATM) - Simulação Bancária em Python

Este projeto é uma aplicação de terminal que simula as operações de um caixa eletrônico, desenvolvida como parte da avaliação de **Programação Orientada a Objetos (POO)**. O sistema permite a criação de contas, depósitos, saques inteligentes com regras de negócio específicas e consulta de histórico.

## Funcionalidades

- **Gerenciamento de Clientes:** Cadastro de nome, CPF e endereço.
- **Tipos de Conta:**
- **Conta Corrente:** Possui limite de cheque especial (R$ 200,00) e taxa de R$ 2,50 para saques após o 4º saque no mês.
- **Conta Poupança:** Rendimento mensal fixo de 2% e limite de 2 saques por mês.
- **Operações Bancárias:** Depósito, Saque e Consulta de Saldo.
- **Histórico:** Listagem detalhada de todas as operações realizadas em cada conta.

## Conceitos de POO Aplicados

Para atender aos requisitos da avaliação, o projeto implementa:

1.  **Pacotes:** Organização modular em `cliente`, `contas` e `operacoes`.
2.  **Encapsulamento:** Uso de atributos protegidos (`_nome`, `_saldo`) e decoradores `@property` para controle de acesso.
3.  **Herança:** As classes `ContaCorrente` e `ContaPoupanca` herdam a lógica base da classe `Conta`.
4.  **Polimorfismo:** O método `sacar()` possui comportamentos diferentes nas subclasses, sendo chamado de forma genérica pela interface.
5.  **Agregação:** A classe `Banco` agrega múltiplos objetos do tipo `Conta`.
6.  **Composição:** Cada `Conta` possui um histórico composto por objetos da classe `Operacoes`, que não existem sem a conta.

## Estrutura do Projeto

```text
banco/
│
├── cliente/
│   └── Cliente.py         # Classe Cliente
├── contas/
│   └── Contas.py          # Classes Banco, Conta, Corrente e Poupança
├── operacoes/
│   └── operacoes.py       # Classe Operacoes (Histórico)
└── main.py                # Ponto de entrada do sistema (Menu)
