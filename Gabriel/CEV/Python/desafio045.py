# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
from colorama import Style, Fore

print(f'''{Fore.CYAN}1 - TESOURA
2 - PEDRA
3 - PAPEL''')
opcoes = ['Tesoura', 'Pedra', 'Papel']

#RESPOSTA HUMANO
jokenpo = opcoes[int(input('Digite qual você vai mandar pra ganhar de mim: '))-1]

#ESPERAR PRA DAR TENSÃO
print(f'\n{Fore.GREEN}- Deixa eu pensar...\n')
sleep(1)

#RESPOSTA PC
resposta = choice(opcoes)
print(f'{Style.BRIGHT}{Fore.CYAN}VOCÊ ESCOLHEU:{Style.RESET_ALL} {jokenpo}')
print(f'{Style.BRIGHT}{Fore.CYAN}EU ESCOLHI:{Style.RESET_ALL} {resposta}\n')
sleep(2)

#TESOURA
if resposta == jokenpo:
    print(f'{Fore.YELLOW}- Empate')
elif jokenpo == 'Tesoura' and resposta == 'Papel':
    print(f'{Fore.GREEN}- Perdi :(')
elif jokenpo == 'Tesoura' and resposta == 'Pedra':
    print(f'{Fore.RED}- Ganhei!')

#PEDRA
elif jokenpo == 'Pedra' and resposta == 'Tesoura':
    print(f'{Fore.GREEN}- Perdi :(')
elif jokenpo == 'Pedra' and resposta == 'Papel':
    print(f'{Fore.RED}- Ganhei!')

#PAPEL
elif jokenpo == 'Papel' and resposta == 'Pedra':
    print(f'{Fore.GREEN}- Perdi :(')
elif jokenpo == 'Papel' and resposta == 'Tesoura':
    print(f'{Fore.RED}- Ganhei!')
sleep(7)