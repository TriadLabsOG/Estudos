# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    lista.append(peso)
maior = max(lista) # Acha o maior valor dentro da lista
menor = min(lista) # Acha o menor valor dentro da lista
print(f'O maior valor lido foi o {maior}, e o menor foi o {menor}')
