# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome completo com todas as letras maiusculas, o nome com todas as letas minusculas, quantas letras tem(sem conssiderar os espaços) e quantas letras tem no primeiro nome

nome = (input('Qual é seu nome completo? ')).capitalize()

divisao = nome.split()

print(f'O seu nome completo todo maiusculo é {nome.upper()}')

print(f'O seu nome completo todo minusculo é {nome.lower()}')
 
print(f'O seu nome tem {len(nome.replace(' ', ''))} caracteres')

print(f'O seu primeiro nome tem {len(divisao[0])} caracteres')