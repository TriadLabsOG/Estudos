# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

contador_maioridade = 0
contador_homens = 0
contador_mulheres = 0
print('Cadastro Python. Seja bem-vindo')

while True:
    print('-' * 30)
    nome = str(input('Digite o nome: ')).capitalize().strip()
    sexo = str(input('Digite o sexo:[Masculino/Feminino] ')).strip().upper()[0]
    if sexo == 'M':
        contador_homens += 1
    idade = int(input('Digite a idade: '))
    if idade > 18:
        contador_maioridade += 1
    if sexo == 'F' and idade > 20:
        contador_mulheres += 1
    resposta = str(input('Você quer continuar cadastrando? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'No total foram cadastrado {contador_maioridade} pessoas com mais de 18 anos,', end= '')
print(f' {contador_homens} homens e {contador_mulheres} mulheres com mais de 20 anos')