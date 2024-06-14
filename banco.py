#criar uma conta bancária para apenas um usuário
#com 3 operações, deposito, saque e extrato 
#todos os depósitos devem ser armazenados em uma variável
#so deve ser permitido 3 saques diários de R$500, caso o usuário não tenha saldo, o sistema deve exebir uma ,mensagem dizendo que não é possivel sacar por falta de dinhero 


menu = """
[d] Depósito
[s] Sacar
[e] Extrato 
[q] Sair
=> """

saldo = 0 
limite = 500 
extrato = ""
numero_saque = 0 
LIMITE_SAQUE = 3


while True: 
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido!")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo 
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operaçaõ falhou! Voçê não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            
        else:
            print("Operação falhou! O valor informado é inválido!")
            
            
    if opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações!") if not extrato else extrato
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")
    
    if opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

