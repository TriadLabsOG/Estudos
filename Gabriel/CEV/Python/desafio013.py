cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }

salario = float(input(f'{cor["cinza"]}Digite o salário:{cor["limpa"]} '))
porcentagem = float(input(f'{cor["cinza"]}Digite a porcentagem de aumento:{cor["limpa"]} '))

aumento = (porcentagem / 100) * salario
salariocorrigido = salario + aumento

print(f'{cor["azul"]}O salário antigo era {cor["verde"]}R${salario:.2f}{cor["azul"]} e o novo é {cor["verde"]}R${salariocorrigido:.2f}{cor["azul"]} com {cor["verde"]}R${aumento:.2f}{cor["azul"]} de aumento.{cor["cinza"]}')
