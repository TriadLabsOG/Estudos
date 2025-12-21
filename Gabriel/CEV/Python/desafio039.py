''' Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import datetime
import colorama

#Ler o ano de nascimento de um jovem
nascimento = int(input(f'{colorama.Fore.LIGHTBLACK_EX}Digite o ano que você nasceu:{colorama.Fore.RESET} '))
idade = datetime.now().year - nascimento

# AINDA VAI SE ALISTAR
if idade < 18:
    print(f'{colorama.Fore.RED}Você é muito novo pra se alistar.{colorama.Fore.RESET}')
    print(f'{colorama.Fore.GREEN}Tente novamente em {nascimento+18}.{colorama.Fore.RESET}')

# HORA EXATA DE SE ALISTAR

elif idade == 18:
    print(f'{colorama.Fore.CYAN + colorama.Style.BRIGHT}Esse é o ano que você deve se alistar.{colorama.Fore.RESET}')

# PASSOU DO TEMPO DE ALISTAMENTO

else:
    print(f'{colorama.Fore.RED}Passou do tempo de alistamento!{colorama.Fore.RESET}')
    print(f'{colorama.Fore.RED}Você deveria ter se alistado em {nascimento+18}{colorama.Fore.RESET}')