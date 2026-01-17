# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
contador_de_tentativas = 0
humano = None

while computador != humano:
    contador_de_tentativas += 1
    humano = int(input("Qual número o computador pensou? "))

print(f"O número do computador era {computador} e você acertou com {contador_de_tentativas} tentativas.")

"""
ANTIGO

from time import sleep
from random import randint

print('- Vou pensar em um número entre 0 a 10')
sleep(2)
print('- Tente advinhar')
sleep(2)

numero_aleatorio = randint(0, 10)

num = int(input('- Qual foi o número que eu pensei? '))
sleep(2)

while num != numero_aleatorio:
    print('- Você errou, tente novamente! ')
    sleep(1)
    num = int(input('- Qual foi o número que eu pensei? '))
print('- Você acertou, parabéns!')
"""