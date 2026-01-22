# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.  No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idade_das_mulheres = 0
idade_do_mais_velho = 0
nome_do_mais_velho = ''
lista_idade = []
for i in range (1, 5):
    print(f'---- {i}ª PESSOA----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    lista_idade.append(idade)
    idade_total = sum(lista_idade)  
    maior_idade = max(lista_idade)
    if i == 1 and sexo in 'Mm':
        idade_do_mais_velho = idade
        nome_do_mais_velho = nome
    if sexo in 'Mm' and idade > idade_do_mais_velho:
        idade_do_mais_velho = idade
        nome_do_mais_velho = nome
    
    if sexo in 'Ff' and idade < 20:
        idade_das_mulheres += 1
media = idade_total / 4
print(f'A media de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idade_do_mais_velho} anos e se chama {nome_do_mais_velho}')
print(f'No total, são {idade_das_mulheres} mulheres com menos de 20 anos')

