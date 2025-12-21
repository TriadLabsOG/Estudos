n1 = float(input('Escreva o primeiro número: '))
n2 = float(input('Escreva o segundo número: '))

print('''1 - Soma
2 - Subtração
3 - Divisão
4 - Multiplicação
''')
n3 = int(input(''))

if n3 == 1:
    soma = n1+n2
    print(soma)
elif n3 == 2:
    sub = n1-n2
    print(sub)
elif n3 == 3:
    div = n1/n2
    print(div)
elif n3 == 4:
    mult = n1*n2
    print(mult)
else:
    print('ERRO: Valor invalido!')