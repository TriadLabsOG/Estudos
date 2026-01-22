# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input('Digite um valor: '))

acumuladora = 0

contadora = 0

while numero != 999:
    
    acumuladora += numero

    contadora +=1
    
    numero = int(input('Digite um valor: '))

print(f'Você digitou {contadora} numeros e a soma de todos eles é {acumuladora}')

