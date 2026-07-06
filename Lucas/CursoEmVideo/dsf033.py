# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))

if n1 > n2 > n3:
    print(f'O número {n1:1f} é o maior e o {n3:1f} é o menor!')

if n1 > n3 > n2:
    print(f'O número {n1:1f} é o maior e o {n2:1f} é o menor!')

if n2 > n3 > n1:
    print(f'O número {n2:1f} é o maior e o {n1:1f} é o menor')

if n2 > n1 > n3:
    print(f'O número {n2:1f} é o maior e o {n3:1f} é o menor')

if n3 > n1 > n2:
    print(f'O número {n3:1f} é o maior e o {n2:1f} é o menor')

else:
    print(f'O número {n3:1f} é o maior e o {n1:1f} é o menor')
    