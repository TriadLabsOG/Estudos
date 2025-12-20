# Exercicio 51
lista = []
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range (1, 10):
    lista.append(termo + (razao * c))
print(termo, end = ', ')
for i in range (0, 9): 
    print(lista[i], end = ', ')
print('FIM!') 