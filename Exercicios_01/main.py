'''Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter 
os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste 
os atributos e métodos implementados.
​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero,
caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."'''

from conta import Conta

temp = Conta()

while True:
    op = int(input('\n\n*********************Menu*********************\n'
                       '1-> Titular\n'
                       '2-> Saldo \n'
                       '3-> Sacar\n'
                       '4-> Depositar\n'
                       '5-> Sair\n'
                       'Escolha :'))
    if op == 1:
        temp.setTitular(str(input('Digite o nome do titular :')))
        temp.titular()
    elif op == 2:
        temp.saldo()
    elif op == 3:        
        saque = float(input('Quanto deseja sacar ? :'))
        temp.sacar(saque)
    elif op == 4:
        deposito = float(input('Qunto deseja depositar ?:'))
        temp.depositar(deposito)
    else:
        break

    
        
    


    