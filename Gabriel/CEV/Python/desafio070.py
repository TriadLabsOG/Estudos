# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

produtos = []
resposta = 's'
id = 0

# LOOP DE PERGUNTAS
while resposta == 's':

    # INPUT DO PRODUTO
    produto = input("DIGITE O NOME DO PRODUTO: ").strip()
    preço = float(input("DIGITE O PREÇO: "))

    # ADICIONA PRODUTO AO DICIONARIO
    produtos[produto] = preço

    # INPUT PRA VOLTAR NAS PERGUNTAS
    resposta = input('DESEJA CONTINUAR (S/N): ').strip().lower()

print(produtos)

# ESTRUTURA LISTA
"""
[
{id: 0,
produto: 'Coca-Cola',
preço: 10.00},
{id: 1,
produto: 'Coca-Cola',
preço: 10.00},
]
"""