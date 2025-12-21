print('='*40)
print('10 TERMOS DE 1 P.A')
print('='*40)

n1 = int(input('Digite o primeiro termo (n1): '))
r = int(input('Digite a razão: '))

for i in range(10):  # Executar o loop 10 vezes
    termo = n1 + i * r  # Calcular o enésimo termo
    print(f'{termo} > ', end='')

print('FIM')