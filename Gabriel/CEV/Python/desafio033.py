#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

num1 = int(input(f'{cor["cinza"]}Digite um número:{cor["limpa"]} '))
num2 = int(input(f'{cor["cinza"]}Digite outro número:{cor["limpa"]} '))
num3 = int(input(f'{cor["cinza"]}Digite o último número:{cor["limpa"]} '))

if num1 > num2 and num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num3:
    menor = num1
elif num2 < num3:
    menor = num2
else:
    menor = num3

print(f'{cor["verde"]}MAIOR NÚMERO: {cor["limpa"]}{maior}')
print(f'{cor["vermelha"]}MENOR NÚMERO: {cor["limpa"]}{menor}')