numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze'
numeros2 = 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
juncao = numeros + numeros2
resposta = int(input('Digite um número entre 0 e 20: '))
if resposta < 0 or resposta > 20: # Se o usuario digitar um numero negativo ou maior do que 20, ira pedir para digitar novamente
    resposta = int(input('Tente novamente. Digite um número de 0 a 20'))
print(f'Você digitou o número {juncao[resposta]}!')