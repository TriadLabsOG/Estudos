cor = {'limpa': '\033[m',
        'azul': '\033[36m',
        'verde': '\033[32m',
        'cinza': '\033[30m'}

numint = int(input(f'{cor["azul"]}Digite um número inteiro:{cor["limpa"]} '))
print(f'{cor["cinza"]}O sucessor de {cor["verde"]}{numint}{cor["cinza"]} é {cor["azul"]}{numint + 1}{cor["cinza"]} e o antecessor é {cor["azul"]}{numint - 1}{cor["cinza"]}.')