# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

p = str(input('Digite uma palavra qualquer: '))

print('Esta palavra é do tipo', type(p))

print('Esta palavra pode ser um alfa? ', p.isalpha())

print('Esta palavra pode ser um número? ', p.isnumeric())

print('Esta palavra pode ser um alfa e/ou um número?', p.isalnum())

print('Esta palavra está inteiramente maiucula? ', p.isupper())

print('Esta palavra está inteiramente minuscula? ', p.islower())
