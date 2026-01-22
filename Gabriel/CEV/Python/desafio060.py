# DESAFIO 060: Cálculo do Fatorial

# Faça um programa que leia um número qualquer e mostre 
# o seu fatorial.

# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite o número: '))

acumulador = numero

while numero != 1:
	numero -= 1
	acumulador = acumulador * numero

print(acumulador)

"""
ANTIGO

numero_input = int(input("Digite o número: "))

numeros = numero_input - 1
resultado = numero_input

print(f'{numero_input}! = {numero_input} x ', end='')
while numeros != 0:
	
	resultado =  resultado * numeros
	if numeros == 1:		
		print(f'{numeros} = {resultado}')
	else:
		print(f'{numeros} x ', end='')
		
	numeros -= 1
"""