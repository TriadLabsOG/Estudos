numeros_pares = list()
numeros_impares = list()
for c in range(0, 7):
    numero = int(input(f'Digite o {c+ 1}º valor: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    elif numero % 2 == 1:
        numeros_impares.append(numero)

print(f'Os números pares são o {numeros_pares}')
print(f'Os números ímpares são {numeros_impares}')
    