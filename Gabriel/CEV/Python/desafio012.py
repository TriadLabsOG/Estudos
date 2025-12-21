cor = {'limpa': '\033[m', # {cor["limpa"]}
        'negativa': '\033[7m', # {cor["negativa"]}
        'azul': '\033[36m', # {cor["azul"]}
        'vermelha': '\033[31m', # {cor["vermelha"]}
        'verde': '\033[32m', # {cor["verde"]}
        'fbranco': '\033[47m', # {cor["fbranco"]}
        'cinza': '\033[30m', # {cor["cinza"]}
        'famarelo': '\033[43m',# {cor["famarelo"]}
        }



preço = float(input(f'{cor["cinza"]}Qual é o preço do produto: {cor["verde"]}R$'))
porcentagem = float(input(f'{cor["cinza"]}Qual a porcentagem de desconto:{cor["verde"]} '))

desconto = (porcentagem / 100) * preço
preçodescontado = preço - desconto

print(f'{cor["azul"]}O produto de {cor["verde"]}R${preço:.2f}{cor["azul"]} vai ter {cor["verde"]}{porcentagem}{cor["azul"]}% de desconto.')
print(f'{cor["azul"]}Sendo assim, ele vai ficar por {cor["verde"]}R${preçodescontado:.2f}{cor["azul"]}, diminuindo {cor["verde"]}R${desconto:.2f}{cor["azul"]} de seu valor.{cor["limpa"]}')