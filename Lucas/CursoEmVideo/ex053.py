# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras e junta tudo sem espaços
palavras = frase.split()
junto = "".join(palavras)

# Inverte a string usando fatiamento (slice), que é bem rápido em Python
inverso = junto[::-1]

print(f'A palavra {junto} ao contrario é {inverso}.')

if inverso == junto:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')