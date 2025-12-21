#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

reta1 = float(input(f'{cor["cinza"]}Digite a primeira reta:{cor["limpa"]} '))
reta2 = float(input(f'{cor["cinza"]}Digite a segunda reta:{cor["limpa"]} '))
reta3 = float(input(f'{cor["cinza"]}Digite a terceira reta:{cor["limpa"]} '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print(f'{cor["verde"]}É possivel existir um triangulo.{cor["limpa"]}')
else:
    print(f'{cor["vermelha"]}Não é possivel existir um triangulo.{cor["limpa"]}')
