'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

#IMPORT DO MODULO RANDOM
from random import randint

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

#FRASES DE EFEITO
print(f'{cor["vermelha"]}-=' + ('--=' * 20))
print(f'{cor["azul"]}Vou pensar em um número entre 0 e 5. Tente advinhar...')
print(f'{cor["vermelha"]}-=' + ('--=' * 20))

#INPUT PRA VARIAVEL QUE PRECISA SER ACERTADA
num = int(input(f'{cor["azul"]}Em que número eu pensei:{cor["limpa"]} '))

#NÚMERO RANDOMICO DE 0 A 5
random = randint(0 , 5)

#CONDICIONAL, SE ACERTAR OU SE ERRAR COM RESPOSTAS DIFERENTES
if num is random:
    print(f'{cor["verde"]}Você está com sorte, o número certo realmente era {num}!{cor["limpa"]}')
else:
    print(f'{cor["vermelha"]}Você digitou {num}, e o número certo era {random}, portanto você infelizmente errou.{cor["limpa"]}')
