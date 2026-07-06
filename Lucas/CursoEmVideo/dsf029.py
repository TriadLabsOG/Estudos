# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Quantos km/h o carro passou? '))

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Este veiculo não foi multado, bom garoto!')
else:
    print(f'Este veiculo foi multado no valor de R${multa}')