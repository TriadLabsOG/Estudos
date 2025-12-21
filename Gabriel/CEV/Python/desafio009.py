cor = {'limpa': '\033[m',
        'negativa': '\033[7m',
        'azul': '\033[36m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'fbranco': '\033[47m',
        'cinza': '\033[30m'}

num = int(input(f'{cor["cinza"]}Digite um número pra ver a tabuada:{cor["limpa"]} '))

print(f'{cor["vermelha"]}-=' * 8)
print(f'{cor["azul"]}{num} x {1:2} = {cor["verde"]}{num*1}')
print(f'{cor["azul"]}{num} x {2:2} = {cor["verde"]}{num*2}')
print(f'{cor["azul"]}{num} x {3:2} = {cor["verde"]}{num*3}')
print(f'{cor["azul"]}{num} x {4:2} = {cor["verde"]}{num*4}')
print(f'{cor["azul"]}{num} x {5:2} = {cor["verde"]}{num*5}')
print(f'{cor["azul"]}{num} x {6:2} = {cor["verde"]}{num*6}')
print(f'{cor["azul"]}{num} x {7:2} = {cor["verde"]}{num*7}')
print(f'{cor["azul"]}{num} x {8:2} = {cor["verde"]}{num*8}')
print(f'{cor["azul"]}{num} x {9:2} = {cor["verde"]}{num*9}')
print(f'{cor["azul"]}{num} x {10:2} = {cor["verde"]}{num*10}')
print(f'{cor["vermelha"]}-={cor["limpa"]}' * 8)