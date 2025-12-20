from random import randint
from time import sleep
computador = randint(0,5) #Fazer o computador "pensar"
print('-=-' * 20)
print('Irei pensar em um número e você ira ter que adivinhar')
print('-=-' * 20)
palpite = int(input('Digite um número de 1 a 5 que você ache que o computador pensou: '))
print('Processando...')
sleep(3)
if palpite != (computador):
    print(f'Você perdeu! Eu pensei no número {computador}')
else:
    print('Você ganhou, parabens!')