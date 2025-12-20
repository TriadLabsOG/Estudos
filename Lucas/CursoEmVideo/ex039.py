ano = int(input('Digite seu ano de nascimento: '))
tempo = 2025 - ano
passou = 2025 - (ano + 18)
ano_alistamento = ano + 18
nao_passou = (ano+18) - 2025
print(f'Quem nasceu em {ano} tem {tempo} anos')
if tempo <18:
    print(f'Você ira se alistar daqui {nao_passou} anos, no ano de {ano_alistamento}')
elif tempo == 18:
    print('Ja esta na hora de se alistar no exercito!')
else:
    print(f'Ja passou o tempo de alistamento a {passou} anos, que foi no ano de {ano_alistamento}')