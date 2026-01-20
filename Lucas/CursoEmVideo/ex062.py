# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0

while contador <= 10:
    print(f'{termo}', end= ' -> ' if contador < 10 else ' -> FIM!')

    termo += razao

    contador += 1

resposta = str(input('Você quer descobrir o proximo termo?[S/N] '))

while resposta == 'S':
    print(f'{termo}')

    termo += razao

    contador += 1

    resposta = str(input('Você quer descobrir o proximo termo?[S/N] '))