expressao = input('Digite: ')
contador = 0

for c in expressao:
    if c == '(':
        contador += 1
    elif c == ')':
        contador -= 1
    if contador < 0:
        break

if contador == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')
