'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso

- Entre 18,5 e 25: Peso Ideal

- 25 até 30: Sobrepeso

- 30 até 40: Obesidade

- Acima de 40: Obesidade Mórbida'''


peso = float(input('Digite seu peso: ')) #CINZA
altura = float(input('Digite sua altura: ')) #CINZA
imc = peso / (altura * altura)

print(F'IMC de {imc:.2f}: ', end='') # AZUL NEGRITO

if imc < 18.5:
    print('Abaixo do peso.') #VERMELHO
elif imc < 25:
    print('Peso ideal.') #AMARELO
elif imc < 30:
    print('Sobrepeso.') #VERDE
elif imc < 40:
    print('Obesidade.') #AMARELO
else:
    print('Obesidade Mórbida.') #VERMELHO