# Crie um programa que leia um número Real e mostre na tela sua porção inteira
from math import trunc
nr = float(input('Digite um número Real: '))

print(f'O número {nr} tem como sua parte inteira {trunc(nr)}')