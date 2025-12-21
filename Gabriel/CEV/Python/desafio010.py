cor = {'limpa': '\033[m', # Limpa as cores
        'negativa': '\033[7m', # Inverte as cores com o fundo
        'azul': '\033[36m', # Cor azul
        'vermelha': '\033[31m', # Cor vermelha
        'verde': '\033[32m', # Cor verde
        'fbranco': '\033[47m', # Fundo branco
        'cinza': '\033[30m', # Cor cinza
        'famarelo': '\033[43m',# Fundo branco
        }

real = float(input(f'{cor["cinza"]}Digite quantos reais você tem na conta:{cor["limpa"]} '))

#No video estava U$3.27
cotação = float(input(f'{cor["cinza"]}Digite quanto o dólar está valendo hoje:{cor["limpa"]} '))

dólar = real / cotação

print(f'{cor["azul"]}Se você converter {cor["verde"]}R${real:.2f}{cor["azul"]} pra dólares, você vai ter {cor["verde"]}U${dólar:.2f}{cor["azul"]}.{cor["limpa"]}')