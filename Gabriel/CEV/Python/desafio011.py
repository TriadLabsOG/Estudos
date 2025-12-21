cor = {'limpa': '\033[m', # Limpa as cores
        'negativa': '\033[7m', # Inverte as cores com o fundo
        'azul': '\033[36m', # Cor azul
        'vermelha': '\033[31m', # Cor vermelha
        'verde': '\033[32m', # Cor verde
        'fbranco': '\033[47m', # Fundo branco
        'cinza': '\033[30m', # Cor cinza
        'famarelo': '\033[43m',# Fundo branco
        }

largura = float(input(f'{cor["verde"]}Digite a largura:{cor["limpa"]} '))
altura = float(input(f'{cor["verde"]}Digite a altura:{cor["limpa"]} '))
area = largura * altura

litros = area/2

print(f'{cor["azul"]}Pra uma area de {cor["verde"]}{area:.1f}m²{cor["azul"]} você vai precisar de {cor["verde"]}{litros:.1f}{cor["azul"]} litros de tinta.{cor["limpa"]}')