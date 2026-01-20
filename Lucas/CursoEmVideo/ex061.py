# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1

while contador <= 10:
    print(f'{termo}', end= ' -> ' if contador < 10 else ' -> FIM!')

    termo += razao

    contador += 1