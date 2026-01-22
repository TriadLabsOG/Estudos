import sys

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

print('Esta são suas opções')
print('--- [1] Soma ---')
print('--- [2] Multiplicar ---')
print('--- [3] Maior ---')
print('--- [4] Novos numeros ---')
print('--- [5] Sair do programa')

escolha = int(input('Qual você vai escolher? '))

while escolha == 4:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite um valor: '))
    escolha = int(input('Qual você vai escolher? '))

while escolha >= 6:
    print('Opção invalida, tente novamente')
    escolha = int(input('Qual você vai escolher? '))

if escolha == 1:
    print(f'a soma de {valor1} + {valor2} é igual a {valor1 + valor2}') # Soma os dois valores digitado

if escolha == 2:
    print(f'O produto entre {valor1} e {valor2} é igual a {valor1 * valor2}') # Multiplica os dois valores digitados

if escolha == 3:
    if valor1 > valor2:
        print(f'O maior valor é o {valor1}')
    elif valor2 > valor1:
        print(f'O maior valor é o {valor2}')
    else:
        ('Os dois valores sao iguais')


if escolha == 5:
    sys.exit()