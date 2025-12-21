# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
import sys
# Quantidade de pessoas.
quantidade_de_pessoas = 4

# Lista pra guardar nomes, idades e sexos com ordem de entrada.
nome = []
idade = []
sexo = []

# Confirmação de quantidade de pessoas e dica pra não confundir o sexo.
print(f'O seu grupo tem {quantidade_de_pessoas} pessoas!\n')
print('(Use H para homem, M para Mulher)')

# Loop pra adicionar tudo nas listas.
for i in range (0, quantidade_de_pessoas):
    sexo.append(str(input(f'Sexo {i+1}ª pessoa: ').upper().strip()))
    if sexo[i] == 'H':
        nome.append(input(f'Nome do {i+1}º: ').strip())
        idade.append(int(input(f'Qual a idade do {nome[i]}: ')))
    elif sexo[i] == 'M':
        nome.append(input(f'Nome da {i+1}ª: ').strip())
        idade.append(int(input(f'Qual a idade da {nome[i]}: ')))
    else:
        print('\nERRO: Use apenas M ou H!\n')
        sys.exit()
    print('\n')

# Média da idade, com base na média aritmetica.
media_idade = sum(idade) / quantidade_de_pessoas

print(f'A média da idade do grupo é: {media_idade} anos.')

# LOOP pra achar quem é o mais velho.
mais_velho = 0
for i in range (0, quantidade_de_pessoas):
    if idade[i] > idade[mais_velho]:
        mais_velho = i

print(f'A pessoa mais velha é: {nome[mais_velho]}')


# Descobrir quantas mulheres têm menos que 20 anos.
menos_que_20 = []
for i in range(0, quantidade_de_pessoas):
    if sexo[i] == 'M' and idade[i] < 20:
        menos_que_20.append(i)

print(f'Mulheres com menos de 20 anos: {len(menos_que_20)}')
