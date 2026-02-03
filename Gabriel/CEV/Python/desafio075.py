# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# Input dos valores inteiros
valores = (
    int(input('Digite o valor 1: ')),
    int(input('Digite o valor 2: ')), 
    int(input('Digite o valor 3: ')), 
    int(input('Digite o valor 4: '))
    )

# A) Quantas vezes apareceu o valor 9.
# Utilizei a função count, ela retorna as ocorrencias de um valor em formato de número inteiro.
print(f'\nO valor "9" aparece {valores.count(9)} vezes.\n')

# B) Em que posição foi digitado o primeiro valor 3.
existe_numero_3 = False
posicao_do_valor = 1

# Loop para adicionar a posição do número 3 na variavel posicao_do_valor
for valor in valores:
    if valor == 3:
        existe_numero_3 = True 
        print(f'O primeiro número "3" está na {posicao_do_valor}ª posição.\n')
        break
    posicao_do_valor += 1

# Condição para saber se existe o número 3
if existe_numero_3 == False:
    print('Não foi encontrado nenhum número 3!\n')

# C) Quais foram os números pares.
lista_pares = []

# Loop para adicionar os números pares em na lista_pares
for valor in valores:
    if valor % 2 == 0:
        lista_pares.append(valor)

# Remove o colchetes da lista
string_pares = str(lista_pares).replace("[", "").replace("]", "")

# Print com verificação se existe número par
if lista_pares:
    print(f'Os valores pares são {string_pares}.')
else:
    print(f'Não foi encontrado nenhum valor par!')
