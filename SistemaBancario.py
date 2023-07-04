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
        print ("Saque")

    elif opcao == "e":
        print ("Extrato")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")              