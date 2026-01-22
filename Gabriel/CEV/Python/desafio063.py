# Exercício 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# ORDEM DA SEQUENCIA 1 1 2 3 5 8 13 21 

termos = int(input("Digite a quantidade de termos: "))

# Duas iterações já que vou adicionar 2 manualmente
iteracoes = 2

numero_a = 0
numero_b = 1

if termos < 1:
    print('ERRO: É preciso ter no minimo 1 termo.')

# Print manual do primeiro termo da sequencia
elif termos == 1:
    print('F0 = 0\n')

# Print manual do primeiro e segundo termo da sequencia
else:
    print('F0 = 0\nF1 = 1')
    while iteracoes != termos:
        print(f'F{iteracoes} = {numero_a + numero_b}')
        # Tuple unpacking ou multipla atribuição
        numero_a, numero_b = numero_b, numero_a + numero_b
        iteracoes += 1

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