cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

celsius = float(input(f'{cor["cinza"]}Digite a temperatura em ºC:{cor["limpa"]} '))
fahrenheit = (celsius * 9 / 5) + 32

print(f'{cor["verde"]}{celsius:.1f}ºC{cor["azul"]} em Fahrenheit é {cor["verde"]}{fahrenheit:.1f}ºF{cor["azul"]}.{cor["limpa"]}')