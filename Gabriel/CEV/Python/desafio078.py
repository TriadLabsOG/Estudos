# Exercício Python 78: Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Logica para ler os 5 valores
lista = []
while len(lista) < 5:
    lista.append(int(input('Digite um valor: ')))

# Ordena a lista do menor para o maior
lista.sort()

# Menor
print(f'MENOR: {lista[0]}')

# Maior
print(f'MAIOR: {lista[-1]}')
