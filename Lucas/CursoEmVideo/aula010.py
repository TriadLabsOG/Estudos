from math import trunc
n1 = float(input('Digite sua primeira nota: '))

n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print(f'Sua media foi de {trunc(media)}')
if media >= 6:
    print('Parabens, você passou de ano!')

else:
    print('Você repitiu de ano!')