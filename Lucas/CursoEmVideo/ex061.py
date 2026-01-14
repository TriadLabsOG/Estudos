termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0

while contador <= 10:
    print(f'{termo}', end= ' -> ' if contador < 10 else ' -> FIM!')

    termo += razao

    contador += 1