import colorama
from colorama import Fore, Style, init
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade >80:
    print(Fore.RED + f'Você foi multado em R${(velocidade-80) * 7}')
else:
    print(Fore.GREEN + 'Você está na velocidade adequeada, continue assim!')