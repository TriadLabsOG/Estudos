#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

#INPUT NA FRASE E STRIP JÁ QUE PRECISAMOS SABER A POSIÇÃO EXATA DO "A"
frase = input(f'{cor["cinza"]}Digite uma frase:{cor["limpa"]} ').strip()

#QUANTAS VEZES APARECE A LETRA "A"

quantidade = frase.count('a')
print(f'{cor["azul"]}QUANTIDADE DE LETRAS "A":{cor["verde"]} {quantidade}')

#frase.lower() PRA REMOVER DIFERENCIAÇÃO DE MAIUSCULA PRA MINUSCULA
#EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ E EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.

print(f'{cor["azul"]}PRIMEIRO: {cor["verde"]}{frase.lower().find("a")}')
print(f'{cor["azul"]}ULTIMO: {cor["verde"]}{frase.lower().rfind("a")}{cor["limpa"]}')
