menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            valor_correto = abs(valor)
            confirmacao = input(f"Você quer depositar R${valor_correto:.2f}? (s/n): ")
            if confirmacao.lower() not in ['s', 'n']:
                print("Operação falhou! O valor informado é inválido.")
            elif confirmacao.lower() == 's':
                saldo += abs(valor_correto)
                extrato += f"Depósito: R$ {valor_correto:.2f}\n"
                print(f"Depósito de R${valor_correto:.2f} realizado com sucesso.")
            else:
                print("Depósito cancelado.")
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Insira o valor do Saque: "))
            valor_correto = abs(valor)
            if valor_correto > saldo:
                print("Saldo insuficiente.")
            elif valor_correto > limite:
                print("Valor de saque maior que o limite.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Número de saques diários atingido.")
            else:
                confirmacao = input(f"Você quer sacar R${valor_correto:.2f}? (s/n): ")
                if confirmacao.lower() not in ['s', 'n']:
                    print("Operação falhou! O valor informado é inválido.")
                elif confirmacao.lower() == 's':
                    saldo -= valor_correto
                    extrato += f"Saque: R$ {valor_correto:.2f}\n"
                    print(f"Saque de R${valor_correto:.2f} realizado com sucesso.")
                    numero_saques += 1
                else:
                    print("Saque cancelado.")
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
       
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
