# Exercicio 52
numero = int(input('Digite um numero: '))
for c in range(1):
    if numero % 1 == 0 and numero % numero == 0:
        print(f'o numero {numero} é um numero primo')
    else:
        print(f'o numero {numero} numero não é um numero primo')    