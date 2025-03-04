saldo = 0

extrato = []

numero_saque = 0

limites_saque = 3 

limite = 500


def Depositar(valor):
    if valor > 0:
        global saldo
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")

def sacar(valor):
        global saldo, numero_saque
        if valor > 0:
               
              if valor > saldo:
                    print("Saldo insuficiente!")
              elif valor > limite:
                    print("valor do saque excede o limite!")
              elif numero_saque >= limites_saque:
                    print("Número máximo de saques excedidos!")
              else:
                  saldo -= valor
                  extrato.append(f"Saque: R$ {valor:.2f}")
                  print("Saque realizado com sucesso!")
                  numero_saque +=1
        else:
            print("Valor do saque inválido") 


def exibir_extrato():
         global saldo
         print("\nextrato:")
         for transacao in extrato:
            print(transacao)
         print(f"Saldo atual: R$ {saldo:.2f}")


while True:
    print("\nOpções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Digite a opçáo desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        Depositar(valor)

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)

    
    elif opcao == "3":
       print("\n-------------EXTRATO----------------") 
       exibir_extrato()
       print("--------------------------------------")
    elif opcao == "4":
         break

    else:
        print("'Opção inválida")

