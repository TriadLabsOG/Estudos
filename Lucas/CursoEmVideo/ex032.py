ano = int(input('Digite um ano e irei analizar ele: '))
bissexto = ano % 4 and ano % 100 != 0 or ano % 400
if bissexto == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print('Este ano não é bissexto')