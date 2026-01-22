# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


lista = []

media_total = 0

acumuladora = 0

resposta = 'S'

while resposta == 'S':
    numero = int(input('Digite um valor: '))
    
    lista.append(numero)
    
    resposta = str(input('Você deseja continuar a digitar valores?[S/N] ')).strip().upper()[0]

    media_total += 1

    acumuladora += numero

    
if len(lista) > 0:
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)

print(f'Você digitou {len(lista)} números, com a media sendo de {media}.', end= '')
print(f'E o maior número foi o {maior} e o menor número foi o {menor}')

