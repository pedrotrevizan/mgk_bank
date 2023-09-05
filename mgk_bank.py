menu = '''
########## Bem vindo ao MGK Bank ##########

[a] Depósito
[b] Saque
[c] Extrato
[d] Sair

Digite a opção desejada: 
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
         valor = float(input("Digite o valor do depósito: "))
             
         if valor > 0:
                saldo += valor
                extrato += f"Depósito - R$ {valor:.2f}\n"
                print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
             
         else : print("Valor depositado precisa ser maior que zero")
    
    elif opcao == "b":
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
             print("Operação não realizada. Saldo disponível excedido")

        elif excedeu_limite:
             print("Operação não realizada. Valor de limite de saque excedido")

        elif excedeu_saque:
             print("Operação não realizada. Quantidade de saques diários excedida")

        elif valor > 0:
             saldo -= valor
             extrato += f"Saque - R$ {valor:.2f}\n"
             numero_saques += 1
             print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")

        else:
             print("Operação falhou. Valor de saque mínimo é de R$ 0,01")
        
    elif opcao == "c":
            if extrato:
                    print(extrato) #exibir a movimentação do extrato acumulado#
            else:
                 print("********** EXTRATO **********")
                 print("\nNenhuma movimentação realizada")
            print(f"\nSaldo R$ {saldo:.2f}")
            print("Obrigado por ser cliente MGK")

    elif opcao == "d":
         print("Encerrando acesso! Obrigado por ser cliente MGK")
         break
    
    else:
         print("Opção inválida, insira uma opção válida")