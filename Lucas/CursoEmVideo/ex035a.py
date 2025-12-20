for v in range(1, 4):
    valor = int(input(f'Digite o {v}º valor: '))
#Verificando quem é o menor
menor = a
if  b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
#Verificando o maior
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'O menor valor é o {menor}')
print(f'O maior valor é o {maior}')