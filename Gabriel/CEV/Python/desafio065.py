# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lista = []
numero = 0
continuar = '.'

while True:
    numero = lista.append(int(input('Digite um número: ')))
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    continuar = '.'

print(f'MÉDIA: {sum(lista) / len(lista):.2f}')
print(f'MAIOR: {max(lista)}')
print(f'MENOR: {min(lista)}')

"""
ANTIGO

numero = 0
maior = 0
# Preciso descobrir como acabar com essa gambiarra KKKKKKKKKKKKKKKKK
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
total_numeros = 0
continuar = ''
erro = True
soma = 0

while continuar != 'N':
    # Input de um número novo a cada loop
    numero = int(input('Digite um número: '))

    # Loop pra saber se é o menor
    if numero < menor:
        menor = numero

    # Loop pra saber se é o maior
    if numero > maior:
        maior = numero

    # Parte do Loop pra tirar a média
    # Soma dos números pra depois tirar a média
    soma += numero
    # Total números
    # Recebe +1 a cada loop pra contar os números
    total_numeros += 1

    
    erro = True
    while erro == True:
        # Input de S ou N pra saber se a pessoa deseja continuar
        continuar = input('Deseja continuar (S/N): ').upper()
        # Condição de continuação
        if continuar != 'N' and continuar != 'S':
            # Se diferente de N ou S, vai retornar um erro e vai repetir o loop
            print('ERRO: Valor invalido!')
        else:
            erro = False

# Print média Aritmética
media = soma / total_numeros
print(f'MÉDIA: {media:.2f}')

# Print maior número
print(f'MAIOR: {maior}')

# Print menor número
print(f'MENOR: {menor}')

# Total de números
print(f'QUANTOS NÚMEROS = {total_numeros}')


# SE TIVER NO PRIMEIRO LOOP, POSSO COLOCAR O UM IF PRA COLOCAR O PRIMEIRO NÚMERO COMO MAIOR OU MENOR PRA TIRAR A GAMBIARRA
"""