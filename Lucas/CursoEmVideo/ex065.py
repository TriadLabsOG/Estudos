numero = int(input('Digite um valor: '))

media_total = 0

acumuladora = 0

resposta = str(input('Você deseja continuar a digitar valores?[S/N]')).capitalize()

while resposta == 'S':
    numero = int(input('Digite um valor: '))

    resposta = str(input('Você deseja continuar a digitar valores?[S/N] ')).capitalize()

    media_total += 1

    acumuladora += numero

print(f'A media de todos os numeros digitados foi de {acumuladora / media_total}')