#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

co = float(input(f'{cor["azul"]}Digite o cateto oposto:{cor["vermelha"]} '))
ca = float(input(f'{cor["azul"]}Digite o cateto adjacente:{cor["vermelha"]} '))
hipot = hypot(co, ca)

print(f'{cor["famarelo"]}{cor["cinza"]}A hipotenusa é {hipot:.2f}{cor["limpa"]}')