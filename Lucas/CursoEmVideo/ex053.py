# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = int(input('Digite uma palavra: '))
for c in range(1):
    frase_invertida = "".join(reversed(frase))
    if frase == frase_invertida:
        print(f'A frase {frase} ao contrario é igual: {frase_invertida}')