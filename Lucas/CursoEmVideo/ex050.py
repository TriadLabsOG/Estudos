lista = []
for c in range(1, 7):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        lista.append(valor)
print(f'Os números pares somados são iguais a {sum(lista)}')