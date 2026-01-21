
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'A quantidade de numeros digitados foram de {contador} e a soma entre eles foi de {soma}')