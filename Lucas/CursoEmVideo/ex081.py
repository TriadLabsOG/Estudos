lista_numeros = []
while True:
    numeros = int(input('Digite um valor: '))
    lista_numeros.append(numeros)
    
    resposta = (input('Você quer continuar a digitar números? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break
    lista_numeros.sort(reverse=True)
print(f'A quantidade de números digitados foram de {len(lista_numeros)}')

print(f'A sequencia de números em ordem decrescente é de {lista_numeros}')
if 5 not in lista_numeros:
    print('O número 5 não foi digitado')
else:
    print(f'O número 5 foi digitado {lista_numeros.count(5)} vezes')