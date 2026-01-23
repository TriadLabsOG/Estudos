import random

numeros = (random.sample(range(1, 11 ), 5))

tupla = tuple(numeros)

print(tupla)


print(f'Os numeros sorteados foram {tupla}')
print(f'O maior número é o {max(tupla)}')
print(f'O menor número é o {min(tupla)}')

