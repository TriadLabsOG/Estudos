cor = {'limpa': '\033[m',
        'negativa': '\033[7m',
        'azul': '\033[36m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'fbranco': '\033[47m',
        'cinza': '\033[30m'}

nota1 = float(input(f'{cor["cinza"]}Digite a primeira nota do aluno:{cor["limpa"]} '))
nota2 = float(input(f'{cor["cinza"]}Digite a segunda nota do aluno:{cor["limpa"]} '))
media = (nota1 + nota2) / 2

print(f'{cor["azul"]}A média das notas do aluno é {cor["verde"]}{media:.1f}{cor["cinza"]}.{cor["limpa"]}')