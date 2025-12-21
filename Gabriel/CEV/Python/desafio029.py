#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

velocidade = int(input(f'{cor["cinza"]}O seu carro está andando a que velocidade:{cor["limpa"]} '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'{cor["vermelha"]}Você vai pagar uma multa de R${multa:.2f}, já que passou {velocidade-80}Km/h do limite da via. {cor["verde"]}(QUE ERA 80KM/H)')
print(f'{cor["azul"]}Tenha um otimo dia, dirija com segurança.{cor["limpa"]}')