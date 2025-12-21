cor = {'limpa': '\033[m',
        'negativa': '\033[7m',
        'azul': '\033[36m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'fbranco': '\033[47m',
        'cinza': '\033[30m'}

num = float(input(f'{cor["azul"]}Digite um numero:{cor["limpa"]} '))
print(f'{cor["cinza"]}O dobro de {cor["verde"]}{num}{cor["cinza"]} é {cor["azul"]}{num*2:.2f}{cor["cinza"]}.\nO triplo de {cor["verde"]}{num}{cor["cinza"]} é {cor["azul"]}{num*3:.2f}{cor["cinza"]}.\nA raiz quadrada de {cor["verde"]}{num}{cor["cinza"]} é {cor["azul"]}{num**(1/2):.2f}{cor["cinza"]}.{cor["limpa"]}')