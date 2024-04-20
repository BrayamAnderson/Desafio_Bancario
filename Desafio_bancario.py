menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

====> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

#Estrutua de repetição
while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("Digite o valor a ser depositado: R$ " ))

        if deposito > 0:

            saldo += deposito

            print(f"O deposito foi de R$ {saldo:.2f}")
            extrato += f"Depósito de R$ {saldo:.2f}\n"

        else:
            print("Valor informado invalido! Tente novamente!")

    elif opcao == "s":

        #Recebe o vlor a ser retirado se o saldo não estiver zerado
        retirada = float(input("Digite o valor do saque: R$ " ))

        #Validações para verificar "Limte", "Saldo" e "Numero de saques"
        excede_saldo = retirada > saldo

        excede_limite = retirada > limite

        excede_saques = numero_saques >= limite_saques

        if excede_saldo:
            print("ERRO! Você não tem saldo suficiente.")

        elif excede_limite:
            print("ERRO! O valor do saque excede o limite.")

        elif excede_saques:
            print("ERRO! Número máximo de saques excedido.")

        elif retirada > 0:
            saldo -= retirada
            extrato += f"Saque de R$ {retirada:.2f}\n"
            numero_saques += 1

        else:
            print("ERRO! Valor informado invalido!")


    elif opcao == "e":

        ## o \n serve para pular a linha abaixo
        print("Sem movimentações na conta." if not extrato else extrato)
        print(f"O seu saldo é R$ {saldo:.2f}\n")
        print("Extrato retirado")

    elif opcao == "q":
        break

    else:
        print(" ERRO!! Por favor selecione novamente a operação desejada.")

