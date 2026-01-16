
numero = int(input('Digite um valor: '))

contador = numero

acumulativo = 1

while contador > 0:
    print(f'{acumulativo}', end= ' -> ' if contador > 1 else ' -> FIM')

    acumulativo *= contador

    contador -= 1


