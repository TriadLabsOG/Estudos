"""
ANTIGO

print('---- Sequencia de Fibonacci ----')

# Input de solicitação de quantos termos serão necessarios printar
termos = int(input('Quantos termos você quer? '))

# ORDEM DA SEQUENCIA 1 1 2 3 5 8 13 21 
n1 = 1
n2 = 0
n3 = 1

while termos != 0:
    n3 = n1 + n2
    print(f'{n1} + {n2} = {n3}')
    n1 = n2
    n2 = n3
    termos -= 1
"""