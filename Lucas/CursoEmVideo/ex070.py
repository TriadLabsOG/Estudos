# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.
produtos_caros = 0
contador = 0
produto_barato = ''
valor_barato = 0
valor_total = 0
while True:
    print('-' * 20)
    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = float(input('Digite o preço do produto: R$'))
    contador += 1 # Conta quantos produtos foram

    valor_total += valor_produto # O valor total se soma com o valor dos produtos

    if valor_produto > 1000: # A cada produto que custa mais de 1000 reais, adiciona 1 no contador  de produtos caros
        produtos_caros += 1

    if contador == 1 or valor_produto < valor_barato:
        valor_barato = valor_produto
        produto_barato = nome_produto

    resposta = str(input('Você quer continuar a digitar produtos? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break
    

print(f'O valor total gasto na compra foi de {valor_total}R$, tendo {produtos_caros} produtos custando mais de 1000R$')
print(f'O produto mais barato custa {valor_barato}R$ e se chama {produto_barato}')