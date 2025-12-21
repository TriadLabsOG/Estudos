cor = {'limpa': '\033[m',
        'negativa': '\033[7m',
        'azul': '\033[0;36m',
        'vermelha': '\033[0;31m'}

print(f'{cor["negativa"]}===== DESAFIO 3 ====={cor["limpa"]}')

numero1 = input(f'{cor["azul"]}Digite o primeiro número pra somar:{cor["limpa"]} ')
if numero1.isnumeric() == True:
    numero1 = int(numero1)
else:
    print(f'{cor["vermelha"]}ERRO: Você só pode digitar números!{cor["limpa"]}')
    exit()

numero2 = input(f'{cor["azul"]}Digite o segundo número pra somar:{cor["limpa"]} ')
if numero2.isnumeric() == True:
    numero2 = int(numero2)
else:
    print(f'{cor["vermelha"]}ERRO: Você só pode digitar números!{cor["limpa"]}')
    exit()

print(f'{cor["azul"]}A soma de {cor["limpa"]}{numero1}{cor["azul"]} com {cor["limpa"]}{numero2}{cor["azul"]} é igual a {cor["limpa"]}{numero1 + numero2}{cor["azul"]}.{cor["limpa"]}')
