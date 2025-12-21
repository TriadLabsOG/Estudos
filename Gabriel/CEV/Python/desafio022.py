'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:'''

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

nome = input(f'{cor["cinza"]}Digite seu nome:{cor["limpa"]} ').strip()

nomedividido = nome.split()

# 1. O nome com todas as letras maiúsculas e minúsculas.
print(nome.lower())
print(nome.upper())

# 2. Quantas letras ao todo (sem considerar espaços).

#GABRIEL OLIVEIRA DOS SANTOS 27 - 3
#GABRIELOLIVEIRADOSSANTOS 24
letras = len(nome) - (len(nome.split()) - 1)
print(letras)

# 3. Quantas letras tem o primeiro nome.

letrasprimeironome = len(nomedividido[0])
print(letrasprimeironome)