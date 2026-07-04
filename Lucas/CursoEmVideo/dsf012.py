# Crie um algoritimo que leia o preço do produto e aplique um desconto de 5%

p = float(input('Digite o valor do produto:R$'))

d = (p * 5) / 100

pd = p - d

print(f'O preço do produto com 5% de desconto foi para {pd}')
