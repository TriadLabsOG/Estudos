# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

# Declaração de variaveis de entrada
pessoa = ' '
idade = 0
sexo = ' '

# Variaveis acumuladoras
mais_de_18 = 0
sexo_masculino = 0
mulheres_menor_que_20_anos = 0

while True:

    pessoa = input("Nome: ").strip
    idade = int(input('Idade: '))
    sexo = input('Sexo (M / F): ').strip().upper()[0]

    if idade >= 19:
        mais_de_18 += 1
    
    if sexo == 'M':
        sexo_masculino += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menor_que_20_anos += 1

    if input('Deseja adicionar mais alguem (S/N): ').strip().upper()[0] == 'N':
        break

print(f'PESSOAS COM MAIS DE 18 ANOS: {mais_de_18}')
print(f'QUANTIDADE DE HOMENS: {sexo_masculino}')
print(f'MULHER COM MENOS DE 20 ANOS: {mulheres_menor_que_20_anos}')

'''
ANTIGO

# Declarei a lista
pessoas = []

# Pessoa 1
pessoa1 = {"nome": input('Nome: '), "idade": int(input('Idade: ')), "sexo": input('Sexo M/F: ')}
pessoas.append(pessoa1)  # Coloca a pessoa1 na caixa

# Mostrando de forma bonita
for pessoa in pessoas:
    print(f"👉 {pessoa['nome']} tem {pessoa['idade']} anos e é do sexo {pessoa['sexo']}")'''
