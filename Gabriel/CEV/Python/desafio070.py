# Exercício Python 70: Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000,00.
# C) Qual é o nome do produto mais barato. 

produto = []
preco = []
index = 0
mais_de_1000 = 0

while True:
    produto.append(input('Digite o nome do produto: '))
    preco.append(int(input('Digite o preço do produto: ')))

    # PRODUTOS QUE CUSTAM MAIS DE 1000
    if preco[index] > 1000:
        mais_de_1000 += 1

    # CONDIÇÃO DE PARADA
    if input('Deseja parar ( S | N ): ').strip().upper()[0] == 'S':
        break
    index += 1


# LOOP PARA DESCOBRIR O MAIS BARATO
index_mais_barato = 0
iteracoes = 0

while True:
    if preco[index] < preco[index_mais_barato]:
        index_mais_barato = index
    if iteracoes == len(produto):
        break
    iteracoes += 1

print(f'PRODUTO MAIS BARATO: {produto[index_mais_barato]}')
print(f'PRODUTOS QUE CUSTAM MAIS QUE 1000: {mais_de_1000}')