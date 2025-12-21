#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
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

real = float(input(f'{cor["cinza"]}Digite um número real:{cor["limpa"]} '))
int = int(math.floor(real))

print(f'{cor["azul"]}O número {cor["verde"]}{real:.2f}{cor["azul"]} após ser arredondado pra um número inteiro vira {cor["verde"]}{int}{cor["azul"]}.{cor["limpa"]}')

#Usando metodo format
#print(f'{real:.0f}')

#Da pra transformat em inteiro usando o int(real)

#Ele usa o math.trunc