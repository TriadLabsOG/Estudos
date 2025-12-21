'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO

- Média entre 5.0 e 6.9: RECUPERAÇÃO

- Média 7.0 ou superior: APROVADO'''
from colorama import Style, Fore

nota1 = float(input(f'{Fore.LIGHTBLACK_EX}Digite uma nota:{Style.RESET_ALL} '))
nota2 = float(input(f'{Fore.LIGHTBLACK_EX}Digite outra nota:{Style.RESET_ALL} '))

media = (nota1 + nota2) / 2

# Média abaixo de 5.0: REPROVADO

if media < 5:
    print(f'{Fore.RED}Sua média foi de {media:.1f} e você está {Style.BRIGHT}REPROVADO{Style.RESET_ALL}{Fore.RED}.{Style.RESET_ALL}')
elif media >= 5 and media < 7:
    print(f'{Fore.RED}Sua média foi de {media:.1f} e você está de {Style.BRIGHT}RECUPERAÇÃO{Style.RESET_ALL}{Fore.RED}.{Style.RESET_ALL}')
elif media >= 7:
    print(f'{Fore.GREEN}Parabens! sua média foi de {Style.BRIGHT}{media:.1f}{Style.RESET_ALL}{Fore.GREEN} Você está {Style.BRIGHT}APROVADO!{Style.RESET_ALL}')