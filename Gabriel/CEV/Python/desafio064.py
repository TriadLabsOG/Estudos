"""
DESAFIO 064: Tratando Vários Valores v1.0

Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. 

No final, mostre quantos números foram digitados e qual foi a soma 
entre eles (desconsiderando o flag 999).
"""
from time import sleep

lista = []
numero = 0
print("DIGITE '999' PARA PARAR!")

while numero != 999:
    numero = int(input('Digite um número: '))
    lista.append(numero)

print('Encerrando', end='', flush=True)
sleep(0.5)

for pontos in range(0, 3):
    print('.', end='', flush=True)
    sleep(0.5)

print(f'\n\nQUANTIDADE DE NÚMEROS DIGITADOS: {len(lista)-1}')
print(f'SOMA: {sum(lista)-999}')

"""
ANTIGO

numero = 0
quantidade_numeros = 0
numero_chave = 0
 
while numero_chave != 999:
    numero_chave = int(input('Digite um número [999 para parar]: '))
    numero += numero_chave
    quantidade_numeros += 1
 
quantidade_numeros -= 1
numero -= 999
 
print(f'Você digitou {quantidade_numeros} números e a soma deles é {numero}')"""