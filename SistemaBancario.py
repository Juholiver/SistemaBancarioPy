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
LIMITES_SAQUES = 3

while true:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito"))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"

        else:

            print ("Operação falhou! Ovalor informado é inválido")
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limiteexcedeu_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" 
            numero_saques += 1
        else:
            print("Operação falhou! o valor informado é inválido.")           
        

    elif opcao == "e":
        print ("Extrato")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")              