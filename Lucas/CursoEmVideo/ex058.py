from random import randint
from time import sleep
computador = randint(0, 10) # O computador pensa em um numero de 0 a 10
print('-'* 20)
print('Irei pensar em um número e você ira ter que adivinhar')
sleep(3)
print('Pensando....')
print('Pensei, agora vamos para o seu palpite')
print('-'* 20)
sleep(3)

escolha = int(input('Qual valor você acha que o computador escolheu? '))
tentativas = 1
while computador != escolha:
    print('Você errou, tente novamente!')
    escolha = int(input('Qual valor você acha que o computador escolheu? '))
    if escolha > 1:
        tentativas += 1
print(f'Você acertou com {tentativas} tentativas')
