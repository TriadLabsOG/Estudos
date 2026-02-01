lista_numeros = []
lista_par = []
lista_impar = []
while True:
    numeros = int(input('Digite um número: '))
    lista_numeros.append(numeros)
    
    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

    resposta = input('Você quer continuar a digitar valores? [S/N] ').strip().upper()[0]

    if resposta == 'N':
        break

print(f'A lista com todos os números é {lista_numeros}')
print(f'A lista com todos os números pares são {lista_par}')
print(f'A lista com todos os números ímpares são {lista_impar}')