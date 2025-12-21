#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

ano = int(input(f'{cor["cinza"]}Digite o ano: {cor["limpa"]}'))

if (ano % 4) == 0:
    print(f'{cor["verde"]}O ano é bissexto.{cor["limpa"]}')
else:
    print(f'{cor["vermelha"]}O ano não é bissexto.{cor["limpa"]}')
