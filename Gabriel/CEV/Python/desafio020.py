#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

cor = {'limpa': '\033[m', # {cor['limpa']}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }


import random

alunos = [input(f"{cor['cinza']}Aluno 1:{cor['limpa']} "), input(f"{cor['cinza']}Aluno 2:{cor['limpa']} "), input(f"{cor['cinza']}Aluno 3:{cor['limpa']} "), input(f"{cor['cinza']}Aluno 4:{cor['limpa']} ")]
random.shuffle(alunos)

print(f"{cor['azul']}A ordem de apresentação é: \n1: {cor['vermelha']}{alunos[0]}\n{cor['azul']}2: {cor['vermelha']}{alunos[1]}\n{cor['azul']}3: {cor['vermelha']}{alunos[2]}\n{cor['azul']}4: {cor['vermelha']}{alunos[3]}{cor['limpa']}")