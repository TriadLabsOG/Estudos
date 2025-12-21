'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
 atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM <= 9

- Até 14 anos: INFANTIL <= 14

- Até 19 anos: JÚNIOR <= 19

- Até 25 anos: SÊNIOR <= 25

- Acima de 25 anos: MASTER > 25'''

from datetime import datetime
from colorama import Style, Fore


ano_nascimento = int(input(f'{Fore.LIGHTBLACK_EX}Qual foi o ano que você nasceu:{Fore.RESET} '))
idade =  datetime.now().year - ano_nascimento


print(f'{Fore.BLACK + Style.BRIGHT}CATEGORIA: {Style.RESET_ALL}', end = '')

if idade <= 9:
    categoria = ' MIRIM'
elif idade <= 14:
    categoria = ' INFANTIL'
elif idade <= 19:
    categoria =  'JÚNIOR'
elif idade <= 25:
    categoria = ' SÊNIOR'
else:
    categoria = ' MASTER'

print(Fore.YELLOW + categoria + Style.RESET_ALL)
