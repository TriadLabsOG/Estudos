cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

dias = int(input(f'{cor["cinza"]}Quantos dias o carro foi alugado:{cor["limpa"]} '))
km = float(input(f'{cor["cinza"]}Quantos KM o carro andou:{cor["limpa"]} '))

preço = (dias * 60) + (km * 0.15)

print(f'{cor["azul"]}O total ficou em {cor["verde"]}R${preço:.2f}{cor["azul"]}.{cor["limpa"]}')