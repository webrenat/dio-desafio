menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 5000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        numero_saques += 1

        if numero_saques > 3:
            print("Não foi possível realizar essa operação! Você excedeu o limite de saque!")
            break

        elif valor < saldo:
            saldo -= valor
            print("Saque realizado com sucesso!")

        elif valor > saldo and valor < limite:
            limite -= valor
            print("Saque realizado com sucesso!")

        else:
            print("Valor indisponível para saque!")

    elif opcao == "e":
        msg = f'''
        ===================== EXTRATO =====================
s
        Hoje foram realizados: {numero_saques} saques.

        Saldo disponível: R$ {saldo:.2f}

        Limite sisponível: R$ {limite:.2f}

        ===================================================
        '''
        print(msg)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione uma opção válida!")

