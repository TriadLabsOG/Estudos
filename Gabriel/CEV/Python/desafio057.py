# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite seu sexo (M/F): ').strip().upper()[0]
while sexo not in "MmFf":
    sexo = input('ERRO: Valor invalido!\nDigite seu sexo novamente (M/F):')
print(f'Sexo: {sexo}')
