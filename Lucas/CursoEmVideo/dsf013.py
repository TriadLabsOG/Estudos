# Crie um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

s = float(input('Digite seu salario:R$ '))

a = (s * 15) / 100

sa = s + a

print(f'Seu salario foi de {s} para {sa} com 15% de aumento')