# Exercício Python 79: Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# LISTA DE NUMEROS
numeros = []

# NUMERO QUE VAI SER ITERADO NA LOOP E ADICIONADO NA LISTA
numero_input = 0

# PRINT INICIAL MOSTRANDO QUE O 'q' PARA A EXECUÇÃO DO CODIGO
print('-' * 40)
print('Digite "q" e de ENTER para parar.')
print('-' * 40)

# LOOP
while True:
    numero_input = input('Digite um valor: ')

    # SE NÃO FOR DIGITO, ENTÃO VAI CAIR NO IF
    if not numero_input.isdigit():
        
        # SE FOR 'q' QUEBRA A EXECUÇÃO
        if numero_input.lower().strip()[0] == 'q':
            break

        # SE NÃO FOR 'q' E NEM UM DIGITO, ENTÃO É UM VALOR INVALIDO
        else:
            print(f'ERRO: O valor digitado é invalido.')

    # SE FOR UM NÚMERO E ELE JÁ ESTIVER NA LISTA, ELE NÃO VAI SER ADICIONADO NA LISTA
    elif int(numero_input) in numeros:
        print(f'ERRO: O valor {numero_input} é duplicado e não vai ser adicionado novamente!')
    
    # SE FOR UM NÚMERO E ELE NÃO ESTIVER NA LISTA, ELE VAI SER ADICIONADO NA LISTA
    else:
        numeros.append(int(numero_input))

# ARRUMA EM ORDEM E PRINTA
numeros.sort()
print(numeros)