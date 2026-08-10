valores = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não irei adicionar!')

    if input('Você quer continuar a digitar mais valores? [S/N]').strip().upper()[0] == 'N':
        break

print(f'Os valores em ordem crescente são {sorted(valores)}')
    