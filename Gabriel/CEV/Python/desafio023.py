# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

nummat = input(f'{cor["verde"]}Digite um número de 0 a 9999: {cor["limpa"]}')

tamanho = len(nummat)

print(f'{cor["azul"]}UNIDADE: {cor["verde"]}{nummat[-1]}{cor["limpa"]}')

if  tamanho >= 2:
    print(f'{cor["azul"]}DEZENA: {cor["verde"]}{nummat[-2]}{cor["limpa"]}')
if  tamanho >= 3:
    print(f'{cor["azul"]}CENTENA: {cor["verde"]}{nummat[-3]}{cor["limpa"]}')
if  tamanho >= 4:
    print(f'{cor["azul"]}MILHAR: {cor["verde"]}{nummat[-4]}{cor["limpa"]}')
