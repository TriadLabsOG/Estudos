# Exercício Python 78: Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Logica para ler os 5 valores
lista = []
while len(lista) < 5:
    lista.append(int(input('Digite um valor: ')))

# Ordena a lista do menor para o maior
lista_arrumada = sorted(lista)

# String para o print
menor = f'O menor numero é {lista_arrumada[0]} e ele aparece nas posiçoes '
maior = f'O maior numero é {lista_arrumada[-1]} e ele aparece nas posições '

for i in range(0, len(lista)):
    # Concatena as posições do menor na string
    if lista[i] == lista_arrumada[0]:
        menor += (f'{i}, ')
    # Concatena as posições do maior na string
    if lista[i] == lista_arrumada[-1]:
        maior += (f'{i}, ')

# Print
print(menor[:-2] + '.')
print(maior[:-2] + '.')