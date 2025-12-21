numeros = []
n1 = int(input('Escreva quantos números você quer somar: '))
for i in range(1, n1+1):
    inteiro = (int(input(f'Digite o {i}º número inteiro: ')))
    if inteiro % 2 == 0:
        numeros.append(inteiro)

print(sum(numeros))
