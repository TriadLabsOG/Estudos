# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nome_do_mais_velho = ''
lista_idade = []
for i in range (1, 5):
    print(f'---- {i}ª PESSOA----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))
    lista_idade.append(idade)
    idade_total = sum(lista_idade)  
    maior_idade = max(lista_idade)
if maior_idade < idade_total:
    print(f'O homem mais velho tem {maior_idade} e se chama {nome_do_mais_velho}')
media = idade_total / 4
print(f'A media de idade do gruo é de {media} anos')

