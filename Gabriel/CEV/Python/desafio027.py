#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#CORES
cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'famarelo': '\033[43m', # {cor["famarelo"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'froxo': '\033[45m',# {cor["froxo"]}
        }

#INPUT PRA CRIAR VARIAVEL COM NOME / STRIP PRA QUANDO EU DIVIDIR NÃO FICAR COM ESPAÇOS / SPLIT PRA PEGAR O PRIMEIRO E ULTIMO ELEMENTO
nome = input(f'{cor["azul"]}Digite um nome:{cor["limpa"]} ').strip().split()

#PRINT NOS PRIMEIRO E ULTIMO NOME
print(f'{cor["froxo"]}PRIMEIRO:{cor["limpa"]} {cor["famarelo"]}{nome[0]}')
print(f'{cor["froxo"]}ULTIMO:{cor["limpa"]} {cor["famarelo"]}{nome[-1]}{cor["limpa"]}')
