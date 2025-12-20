ano = int(input('Qual é o ano de nascimento do aluno? '))
idade= 2025 - ano
print(f'O atleta tem {idade} anos')
if idade <=9:
    print('O nadador ira ter o plano mirim')
elif idade >=10 and idade <=14:
    print('O nadador ira ter o plano infantil')
elif idade >=15 and idade <=19:
    print('O nadador ira ter o plano junior')
elif idade <=20:
    print('O nadador ira ter o plano sênior')
else:
    print('O nadador ira ter o plano master')