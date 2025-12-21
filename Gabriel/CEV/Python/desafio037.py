# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
# Conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('\033[30mDIGITE O NÚMERO PRA SER TRANSFORMADO: \033[m'))
inp = input('\033[30m◉ 1 PARA BINÁRIO\n◉ 2 PARA OCTAL\n◉ 3 PARA HEXADECIMAL\nDIGITE: \033[m')

if inp == '1':
    print(f'\033[34mSeu número em binário é: \033[35m{bin(num)}\033[m')
elif inp == '2':
    print(f'\033[34mSeu número em octal é: \033[35m{oct(num)}\033[m')
elif inp == '3':
    print(f'\033[34mSeu número em hexadecimal é \033[35m{hex(num)}\033[m')
else:
    print('\033[31mOPÇÃO INVALIDA!\033[m')