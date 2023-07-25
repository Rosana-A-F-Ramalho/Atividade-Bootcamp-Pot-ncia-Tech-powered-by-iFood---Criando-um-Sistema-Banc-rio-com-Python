menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito = R${valor:.2f}\n"
            print("Deposito Realizado\n")
            
        else:
            print("Operação Falhou, valor informado é invalido")    

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, valor de saque informado maior que saldo disponivel.")

        elif excedeu_limite:
            print("Operação falhou, valor de saque informado maior que limite de saque.")

        elif excedeu_saques:
            print("Operação falhou, numeros de saques diarios excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado!")

        else:
            print("Valor informado invalido")    

    elif opcao == "e":
        print("====== EXTRATO ======")
        print("Não há movimentação para o periodo" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "q":
        break

    else:
        print("Operacão inválida, por favor selecione novamente a opção desejada.")

