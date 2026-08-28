dados = list()
dados_totais = list()
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    # Pega o nome e o peso e adiciona em uma lista
    
    if len(dados_totais) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    dados_totais.append(dados[:]) 
    dados.clear()
    # Copia a lista dados para uma lista de dados totais e apaga a dados

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-' * 40)
print(f'Ao todo, você cadastrou {len(dados_totais)} pessoas.')


print(f'O maior peso foi de {maior_peso}kg. Peso de: ', end='')
for p in dados_totais:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()


print(f'O menor peso foi de {menor_peso}kg. Peso de: ', end='')
for p in dados_totais:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')

