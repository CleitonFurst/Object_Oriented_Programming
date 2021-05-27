from tv import Tv 

temp = Tv()
valor = 0
volume = 0 
while True:
    op = int(input('\n\n*********************Menu*********************\n'
                       'Canal\n1-> Proximo\n'
                       '2-> Voltar \n'
                       '3-> Digitar canal\n'
                       'Volume\n4-> Almentar\n'
                       '5-> Diminuir\n'
                       '6-> Digitar volume\n'
                       '7-> Desligar TV\n'
                       'Escolha :'))
    if op == 1:
        valor += 1
        temp.mudacanal(valor)        
    elif op == 2:
        valor -= 1
        temp.mudacanal(valor)
    elif op == 3:
        valor = int(input('Digite o canal :'))    
        temp.canal(valor)
    elif op == 4:
        volume += 1
        temp.volume(volume)
    elif op == 5:
        volume -= 1
        temp.volume(volume)
    elif op == 6:
        volume = int(input('Digite o valor do volume:'))
        temp.volume(volume)
    else:
        break