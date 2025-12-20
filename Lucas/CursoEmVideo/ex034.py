salario = float(input('Qual é seu salario atual? '))
if salario >1250:
    print(f'Seu novo salario com 10% de aumento ira ser de {(salario + (salario * 0.10))}')
else:
    print(f'Seu novo salario com 15% de aumento ira ser de {(salario + (salario * 0.15))}')