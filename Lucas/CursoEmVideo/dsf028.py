# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

computador = randint(0, 5)

print('Pensei em um valor de 0 a 5, tente adivinhar qual')

escolha_jogador = int(input('Qual é o número que eu pensei? '))

if escolha_jogador == computador:
    print('Boa mlk, você acertou o número que eu pensei')

else:
    print(f'Seu otario, eu pensei no número {computador}')
