
# ANTIGO

print('='*40)
print('10 TERMOS DE 1 P.A')
print('='*40)

n1 = int(input('Digite o primeiro termo (n1): '))
r = int(input('Digite a razão: '))

for i in range(n1, 10 * r + 1, r):
    print(f'{i} > ', end='')
print('FIM')