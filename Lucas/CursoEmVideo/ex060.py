# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120


numero = int(input('Digite um valor: '))

contador = numero

acumulativo = 1

while contador > 0:
    print(f'{acumulativo}', end= ' -> ' if contador > 1 else ' -> FIM')

    acumulativo *= contador

    contador -= 1


