#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

#Distância de uma viagem em Km
distancia = int(input(f'{cor["cinza"]}Digite a distancia da viagem: {cor["limpa"]}'))

#Preço da passagem
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'{cor["azul"]}O valor da passagem fica em {cor["verde"]}R${valor:.2f}{cor["azul"]}.')
