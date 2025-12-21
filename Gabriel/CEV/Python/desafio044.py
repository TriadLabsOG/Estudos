'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto

- à vista no cartão: 5% de desconto

- em até 2x no cartão: preco normal

- 3x ou mais no cartão: 20% de juros'''


from sys import exit as sys_exit

preco = float(input('Qual é o preço do produto: R$'))

print('''DIGITE 1 - À VISTA DINHEIRO/CHEQUE
DIGITE 2 - DEBITO OU CRÉDITO À VISTA
DIGITE 3 - CRÉDITO PARCELADO''')

pagamento = input('Qual a forma de pagamento: ')

com = ''
# 10% de desconto
if pagamento  == '1':
    preco -= (preco * (10/100))
    com = r' com 10% de desconto'
# 5% de desconto
elif pagamento == '2':
    preco -= (preco * (5/100))
    com = r' com 5% de desconto'
# Parcelado
elif pagamento == '3':
    prestacoes = int(input('Quantas vezes (Até 10x): '))
    if prestacoes in {3, 4, 5, 6, 7, 8, 9, 10}:
        preco += (preco * (20/100)) # JUROS
        com = r' com 20% de júros'
    elif prestacoes >= 11:
        print('ERRO: Você só pode parcelar até 10x')
        sys_exit()

print(f'O valor{com} ficou em R${preco:.2f}.')
