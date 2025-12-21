# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

quantidade_de_pessoas = 5
# INPUT DO NOME DAS PESSOAS E ADICIONANDO NA LISTA DE NOMES
nome_das_pessoas = []
for i in range (0, quantidade_de_pessoas):
    nome_das_pessoas.append(input(f'Qual é o nome da {i+1}ª pessoa: '))

# PESO DAS PESSOAS COM BASE DO NOME DELES NA LISTA DE NOMES
peso_das_pessoas = []
for i in range(0, quantidade_de_pessoas):
    peso_das_pessoas.append(float(input(f'Quantos quilos {nome_das_pessoas[i]} tem: ')))

# TESTAR QUAL O MAIOR E MENOR PESO DA LISTA DE PESO E GUARDAR O INDEX

pessoa_mais_leve = min(peso_das_pessoas)
pessoa_mais_pesada = max(peso_das_pessoas)

leve = []
for i in range (0, quantidade_de_pessoas):
    if pessoa_mais_leve == peso_das_pessoas[i]:
        leve.append(nome_das_pessoas[i])

pesada = []
for i in range(0, quantidade_de_pessoas):
    if pessoa_mais_pesada == peso_das_pessoas[i]:
        pesada.append(nome_das_pessoas[i])

print(f'LEVE: {leve}')
print(f'PESADA: {pesada}')
