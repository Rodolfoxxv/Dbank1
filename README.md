# Dbank1 - Versão 1.0
# Projeto de Sistema Bancário

Este é um projeto simples de sistema bancário feito com Python, onde o usuário realizar pode realizar operações como depósito, saque e visualização de extrato. Incluindo validações para garantir que os valores são válidos.

## Funcionalidades

- **Depositar**: Permite ao usuário depositar um valor na conta.
- **Sacar**: Permite ao usuário sacar um valor da conta, respeitando o saldo disponível, o limite de saque e o número máximo de saques diários.
- **Extrato**: Exibe o extrato das movimentações realizadas na conta.
- **Sair**: Encerra o programa.

## Destaque: Função `abs`

A função `abs` garante que o depósito e o saque sejam sempre positivos, mesmo que o valor fornecido pelo usuário seja negativo. Isso garante a integridade das operações.

```python
valor = float(input(f"Insira o valor do Depósito: "))
valor_correto = abs(valor)
```

## Como Clonar Repositório e Instalar Python

- **Passo 1:** Selecionar Local Para Clonar
Primeiro, selecione a pasta no seu computador onde você deseja clonar o repositório.

- **Passo 2:**  Clonar o Repositório
Abra o Git Bash ou o cmd no seu terminal e execute o seguinte comando:

git clone https://github.com/Rodolfoxxv/Dbank1.git

- **Caso não tenha o Python:** 
Baixe verção para o seu sitema operacional no link: https://www.python.org/downloads/



