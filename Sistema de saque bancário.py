menu = '''

[4] Depositar
[3] Sacar
[2] Extrato
[1] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "4":
        valor = float(input("Informe o valor de depósito: ")) 

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: O valor informado é inválido.")

    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))
    
    if valor > 0:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação fahou!Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede limite.")
        elif excedeu_saques:
            print("Operação falhou! Número maximo de saques excedido.")
       
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou!O valor informado é inválido.")


    if opcao == "2": 
        print("\n######### EXTRATO #########")
        print("Nenhuma movimentação foi realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###########################")

    elif opcao == "1":  
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")


