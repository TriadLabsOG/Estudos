# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salario para o seu aumento: '))

if salario >= 1250.00:
    print(f'Seu novo salario ira ser de {(salario) + salario * 10  / 100 }')
else:
    print(f'Seu novo salario ira ser de {(salario) + (salario * 15) / 100}')