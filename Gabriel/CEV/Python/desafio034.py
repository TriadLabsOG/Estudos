#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

salario = int(input(f'{cor["cinza"]}Digite seu salario:{cor["limpa"]} '))

if salario > 1250:
    porcentagem = 10
    relacao = (f'{cor["vermelha"]}superior')
else:
    porcentagem = 15
    relacao = ('inferior')

aumento = (porcentagem / 100) * salario
salarionovo = aumento + salario

print(f'{cor["azul"]}Você vai receber um aumento de {cor["verde"]}{porcentagem}%{cor["azul"]} pois seu salario é {relacao} a {cor["verde"]}R$1250,00')
print(f'{cor["azul"]}Sendo assim você vai receber {cor["verde"]}R${salarionovo:.2f}{cor["limpa"]}')