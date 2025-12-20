# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
lista = []
for i in range(1, 8):
    ano_de_nascimento = input(f'Digite o ano de nascimento da {i}ª pessoa: ')
    idade_atual = 2025 - int(ano_de_nascimento) # Calcula a idade da pessoa
    if idade_atual >= 18:
        lista.append(ano_de_nascimento)
resultado = ", ".join(lista)
print(f'as pessoas que tem mais de 18 anos nasceram no ano de {resultado}')