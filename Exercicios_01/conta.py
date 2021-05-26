class Conta:
    def __init__(self):
        self.__titular = None   
        self.__saldo = 0


    def setTitular(self,titular):
        self.__titular = titular


    def getTitular(self):
        return self.__titular
    

    def setSaldo(self,saldo):
        self.__saldo = saldo


    def getSaldo(self):
        return self.__saldo
     
        
    def saldo(self):
        valor = self.getSaldo() 
        print(f'Saudo atual R${valor:.2f}')
     
        
    def titular(self):
        titular = self.getTitular()
        print(f'Titular da conta {titular}')
      
        
    def sacar(self, saque):
        if saque != 0:
            if self.getSaldo() > saque:        
                valor = self.getSaldo() - saque
                self.setSaldo(valor)
                valor = self.getSaldo()
                print(f'Saldo atual R${valor:.2f}')
            else:
                valor = self.getSaldo()
                print(f'Você não tem saldo suficiente para essa operação !!!!')
                print(f'Saldo atual R${valor:.2f}')
        else:
            print('Você não pode sacar ) reais !!!')
      
        
    def depositar(self, deposito):       
        validar = str(input(f'O valor R${deposito} esta correto ? (S/N)').strip().upper()[0])
        if validar == 'S':
            valor = self.getSaldo()
            self.setSaldo(valor + deposito)
            valor = self.getSaldo()
            print(f'Saldo atual R${valor:.2f}')
        else:
            print('Operação cancelada com sucesso !!!')
            
        

        