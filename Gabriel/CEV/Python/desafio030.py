#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

#INPUT NO NÚMERO (PRECISA SER STRING PORQUE INTEIRO É IMUTAVEL E PRECISAMOS MUDAR DEPOIS).
num = input(f'{cor["cinza"]}Digite um número inteiro:{cor["limpa"]} ')

#PEGANDO O ULTIMO NÚMERO DA STRING E TRANSFORMANDO EM INTEIRO NOVAMENTE.
ultimonumero = int(num[-1])


#TESTANDO PRA VER SE O NÚMERO É IMPAR OU PAR E PRINTANDO RESULTADO.
if ultimonumero in (1, 3, 5, 7, 9):
    print(f'{cor["azul"]}Seu número é impar.{cor["limpa"]}')
else:
    print(f'{cor["azul"]}Seu número é par.{cor["limpa"]}')
