cor = {'limpa': '\033[m',
        'negativa': '\033[7m',
        'azul': '\033[36m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'fbranco': '\033[47m',
        'cinza': '\033[30m'}

metros = float(input(f'{cor["vermelha"]}Digite os metros:{cor["azul"]} '))
centimetros = metros * 100
milimetros = centimetros * 10

print(f'{cor["azul"]}Centimetros: {cor["verde"]}{centimetros:.2f}{cor["azul"]}.\nMilimetros: {cor["verde"]}{milimetros:.2f}{cor["azul"]}.{cor["limpa"]}')