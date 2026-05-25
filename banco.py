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

        deposito = float((input("Digite o valor que deseja depositar: ")))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R$: {deposito:.2f}\n"
            print(f"Depositou R${deposito:.2f} reais")
        else:
            print("Valor inválido para depósito")
       

    elif opcao == "s":

        saque = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")

        elif excedeu_limite:
            print("O valor do saque excede o limite")

        elif excedeu_saques:
            print("Número máximo de saques excedido")

        elif saque > 0:
            
            saldo -= saque 
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print(f"Sacou R${saque:.2f} reais")
        
        else:
            print("Valor inválido para saque")

    elif opcao == "e":

        print(f"=============== EXTRATO ===============")

        if not extrato:
            print("Não foram realizadas movimentações")

        else:
            print(extrato)

        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")