# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos quilometros você rodou neste carro? '))

d = int(input('Quantos dias você rodou neste carro? '))

dr = 60 * d

kmr = 0.15 * km

pt = dr + kmr

print(f'No total, você ira pagar R${pt}')