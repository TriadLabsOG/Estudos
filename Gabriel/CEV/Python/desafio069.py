# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

#pessoa, idade, sexo = input("Nome: "), input('Idade: '), input('Sexo: ')


# Declarei a lista
pessoas = []

# Pessoa 1
pessoa1 = {"nome": input('Nome: '), "idade": int(input('Idade: ')), "sexo": input('Sexo M/F: ')}
pessoas.append(pessoa1)  # Coloca a pessoa1 na caixa

# Mostrando de forma bonita
for pessoa in pessoas:
    print(f"👉 {pessoa['nome']} tem {pessoa['idade']} anos e é do sexo {pessoa['sexo']}")
