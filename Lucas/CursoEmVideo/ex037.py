import sys
num = int(input('Digite um numero para conversão: '))
escolha = int(input('Escolha 1 para binario, 2 para octal ou 3 para hexadecimal: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if escolha == 1:
    print(f'O número {num} em codigo binario é {hexadecimal} ')
elif escolha == 2:
    print(f'O número {num} em codigo octal é {octal}')
elif escolha == 3:
    print(f'O número {num} em codigo hexadecimal é {hexadecimal}')
else:
    print('Opção invalida!')
    sys.exit()
