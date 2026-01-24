valores = []

contador = 0

while contador != 5: # Eu fiz de uma maneira mais complexa para eu praticar mais o while
    valor = float(input('Digite um valor: '))
    valores.append(valor)
    contador += 1

menor = min(valores)

maior = max(valores)

print(f'O maior valor digitado foi o {maior} e o menor foi o {menor}!')