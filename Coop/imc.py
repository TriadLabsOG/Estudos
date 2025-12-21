''' Exercício 2: Calculadora de IMC (Simples)
Objetivo: Trabalhar no mesmo arquivo sem conflito (edição sequencial).

Dev A: Cria imc.py. Faz a parte que pede o Peso e a Altura do usuário (float). Comita e Push.

Dev B: Dá git pull. Adiciona o cálculo: imc = peso / (altura ** 2). Imprime o valor do IMC na tela. Comita e Push.

Dev A: Dá git pull. Adiciona as condições (if imc < 18.5: print("Abaixo do peso"), etc.). Comita e Push. '''

# Print inicial
print('Para calcular seu IMC:')

# Inputs
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (cm): '))

# Logica
    # Converter altura para metros

altura_em_metros = altura / 100

    # IMC
imc = peso / altura_em_metros ** 2

print(f'Seu IMC é {imc}')
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc < 30:
    print('Você está no peso ideal')
elif imc < 40:
    print('Você está lidando com sobrepeso')
elif imc > 40:
    print('Você esta em obesidade mórbida')

# TESTE