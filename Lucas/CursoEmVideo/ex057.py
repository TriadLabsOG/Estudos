sexo = str(input('Qual é o seu sexo?[M/F] ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Errado! Digite seu sexo novamente')
    sexo = str(input('Qual é o seu sexo?[M/F] ')).strip().upper()
print('Seus dados estão corretos!')