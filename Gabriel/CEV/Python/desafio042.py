'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

# COMPROVA EXISTENCIA DE TRIANGULOS
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Existe um triangulo ', end='')
    # COMPROVA QUE ELE É EQUILATERO PELA IGUALDADE DE TODOS OS LADOS
    if r1 == r2 and r2 == r3:
        print('equilátero.')
    # COMPROVA QUE É ISÓSCELES CASO ELE NÃO SEJA EQUILÁTERO.
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('isósceles.')
    # SE NENHUM LADO FOR IGUAL ENTÃO É ESCALENO.
    else:
        print('escaleno.')
# SE NÃO EXISTIR TRIANGULO.
else:
    print('Não é possivel existir um triângulo.')
