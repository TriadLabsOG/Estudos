# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))

divisao = nome.split()

print(f'Seu primeiro nome é {divisao[0]} e seu ultimo nome é {divisao[len(divisao) -1]}')