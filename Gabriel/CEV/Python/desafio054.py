# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'
import datetime

# Ano atual com o modulo datetime
ano_atual = datetime.date.today()
ano_atual = ano_atual.year

# Input na quantidade de pessoas pra saber a quantidade de loops que vamos fazer
quantidade_pessoas = int(input('Quantas pessoas que são: '))
# Condição pra não passar de 10 no limite da quantidade de inputs, assim não ficando muito pesado.
if quantidade_pessoas > 10:
    print('Limite de pessoas excedido!')
else:

    # Lista com nomes e anos
    nomes = []
    anos = []
    lista_maioridade = []

    #Loop de input indentado nas listas
    for i in range(0, quantidade_pessoas):
        nomes.append(input(f'Qual é o {i+1}º nome: '))
        anos.append(int(input(f'Qual foi o ano de nascimento do {i+1}º: ')))
    
    # Loop de condicional na formula (ano - nascimento = idade > 18)
    for i in range(0, quantidade_pessoas):
        if (ano_atual - anos[i]) > 18:
            lista_maioridade.append(i)
    if lista_maioridade == []:
        print('Ninguém é de maior!')
    else:
        for i in range(0, len(lista_maioridade)):
            print(f'{i+1}º {nomes[lista_maioridade[i]]} {anos[lista_maioridade[i]]}')
