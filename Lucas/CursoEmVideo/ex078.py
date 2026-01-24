valores = []


for v in range(0, 5):
    valor = int(input('Digite um valor: '))

    valores.append(valor)

print(f'O maior número foi o {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor número foi o {min(valores)} na posição {valores.index(min(valores))}')

    


