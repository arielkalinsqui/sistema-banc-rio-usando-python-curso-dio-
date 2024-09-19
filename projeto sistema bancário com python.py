menu = '''

[d] depositar 
[s] sacar
[e] extrato
[q] sair


=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while  True:


    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('informe o valor do deposito\n'))
                          
    

        if valor > 0:
         saldo += valor 
         extrato += f'deposito de R$ {valor:2f}\n'

        else: 
          print ('operação falhou: o valor informado é inválido')


    elif opcao == 's':

     valor = float(input('informe o valor do saque\n:'))
     

     excedeu_saldo = valor > saldo

     excedeu_limite = valor > limite

     excedeu_saques = numero_saques >= limite_saques
      

     if excedeu_saldo:
         print('operação falhou! Você não tem saldo suficiente!')

     elif excedeu_limite:
           print('operação falhou! o valor excede o seu limite diário.')

     elif valor > 0:
         saldo -= valor 
         extrato += f'saque: R$ {valor:.2f}\n'
         numero_saques += 1
    
     
     else:
          print ('operação falhou! o valor informado é invalido!')

    

    elif opcao == 'e':   
        print ('\n================ EXTRATO ==================')
        print ('não foram realizadas movimentas bancárias' if not extrato else extrato)
        print (f'\nSaldo: R$ {saldo:.2f}')
        print ('=========================================')


    elif opcao == 'q':
        break


    else:
        print('operação inválida, por favor selecione novamente a operação desejada.')





