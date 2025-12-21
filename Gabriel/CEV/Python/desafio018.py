#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

grau = float(input(f'{cor["cinza"]}Digite um angulo: {cor["limpa"]}'))

radiano = math.radians(grau)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'{cor["azul"]}SENO: {cor["vermelha"]}{seno:.2f}')
print(f'{cor["azul"]}COSSENO: {cor["vermelha"]}{cosseno:.2f}')
print(f'{cor["azul"]}TANGENTE {cor["vermelha"]}{tangente:.2f}{cor["limpa"]}')
