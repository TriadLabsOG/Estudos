lista = []
for c in range(3, 500, 3):
    if c % 2 == 1:
        lista.append(c)
print(f'a soma de todos os numeros multiplo de 3 é igual a {sum(lista)}')