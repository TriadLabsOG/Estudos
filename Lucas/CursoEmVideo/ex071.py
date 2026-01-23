# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print('-' * 30)
print('Banco Digital')
print('-' * 30)
sleep(2.5)
print('Ola senhor(a)')
sleep(2.5)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
nota_atual = 50
total_notas = 0

while True:
    if total >= nota_atual:
        total -= nota_atual
        total_notas += 1
    else:
        if total_notas > 0:
            print(f'Foram no total de {total_notas} notas de R${nota_atual}')
        
        if nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 1


        total_notas = 0
        if total == 0:
            break

print('-' * 30)
print('Saque finalizado. Volte sempre!')