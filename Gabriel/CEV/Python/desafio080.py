# Exercício Python 80: Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista de números
lista_numeros = []

# Adiciona 5 números a lista
while len(lista_numeros) != 5:
    lista_numeros.append(int(input(f"Digite o {len(lista_numeros)+1}º número: ")))

# Itera sobre os números (0, 4)
for index in range(len(lista_numeros) - 1):
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i] > lista_numeros[i + 1]:
            lista_numeros[i], lista_numeros[i + 1] = lista_numeros[i+1], lista_numeros[i]

print(lista_numeros)
