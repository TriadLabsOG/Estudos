# Crie um programa que leia o nome completo de uma pessoa e diga se tem "Silva" no nome.

nome = str(input('Digite seu nome completo: '))

if 'Silva' in nome:
    print('Seu nome tem Silva, você é brasileiro')
else:
    print('Seu nome não apresenta Silva')