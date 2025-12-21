#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

a1 = input(f'{cor["cinza"]}Digite o nome do primeiro aluno:{cor["limpa"]} ')
a2 = input(f'{cor["cinza"]}Digite o nome do segundo aluno:{cor["limpa"]} ')
a3 = input(f'{cor["cinza"]}Digite o nome do terceiro aluno:{cor["limpa"]} ')
a4 = input(f'{cor["cinza"]}Digite o nome do quarto aluno:{cor["limpa"]} ')

print(f'{cor["azul"]}O aluno sorteado foi {cor["verde"]}{random.choice([a1, a2, a3, a4])}{cor["azul"]}.{cor["limpa"]}')

