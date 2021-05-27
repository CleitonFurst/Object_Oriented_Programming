'''Exercicio para treinar ABSTRAÇÃO e ENCAPSULAMENTO:

Faça um programa que simule um televisor criando-o como um objeto. ​
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.​
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.​
'''
class Tv:
    def __init__(self):
        self.__canais = ((2	,'Cultura'),
                        (4,	'SBT SP'),
                        (5,	'Globo SP'),
                        (7,	'Record SP'),
                        (9,	'RedeTV!'),
                        (11,'TV Gazeta'),
                        (13,'Band SP'),
                        (14,'Mix TV'),
                        (16,'Mega TV'),
                        (19,'GloboNews'),
                        (21,'Rede 21 – TV Mundial'),
                        (25,'TVCi – TV Mundial'),
                        (27,'CNT SP'),
                        (32,'MTV Brasil'),
                        (34,'Rede Vida'),
                        (36,'Esporte Interativo'),
                        (40,'TV Sul Bahia – RIT'),
                        (42,'Record News'),
                        (44,'Boas Novas'),
                        (44,'Oeste TV – TV União'),
                        (45,'TV ABC – RBTV'),
                        (46,'TV Novo Tempo'),
                        (48,'NGT'),
                        (50,'Rede Brasil'),
                        (51,'TV Aparecida'),
                        (52,'Top TV'),
                        (53,'Rede Gospel'),
                        (57,'TV União'),
                        (58,'J.R. Comunicações'),
                        (59,'J.R. Comunicações'),
                        (62,'TV Brasil')                        
                                        )
        
        self.__volume = 100
        
    def canal(self,valor):
        canal = None
        for i in self.__canais:
            if valor != i[0]:
               canal = 0
            elif valor == i[0]: 
                canal = 1               
                print(f'Assitindo ao canal {i[0]} - {i[1]}')
                break
            else:
                continue
        if canal == 0:
             print('Canal invalido !!!')
        
    
    def mudacanal(self,valor):        
        valor -= 1
        if valor < 0:
            valor = len(self.__canais)
        elif valor > len(self.__canais):
            valor = 0
        else:
            pass
        print(f'Canal {self.__canais[valor]}')
        
    def volume(self,valor):
        if valor >= self.__volume:
            print(f'Volume máximo')
            print(f'Volume 0 ',end='') 
            print('|'*self.__volume, self.__volume)    
        elif valor  <= 0:
            print(f'Mudo !!!')
            print(f'Volume 0 ',end='') 
            print('.'*self.__volume,self.__volume)      
        else:
            print(f'Volume 0 ',end='') 
            print('|'*valor,end='')            
            print('.'*(self.__volume - valor), self.__volume) 
            
             
              
             
                
        