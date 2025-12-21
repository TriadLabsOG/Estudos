'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

- O primeiro valor é maior

- O segundo valor é maior

- Não existe valor maior, os dois são iguais'''

num1 = int(input('\033[30mDigite um número inteiro: \033[m'))
num2 = int(input('\033[30mDigite outro número inteiro: \033[m'))

if num1 > num2:
    print(f'\033[35mO número {num1} é maior que o {num2}.\033[m')
elif num2 > num1:
    print(f'\033[35mO número {num2} é maior que o {num1}.\033[m')
else:
    print(f'\033[31mOs números são iguais.\033[m')