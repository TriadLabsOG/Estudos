quantidade = int(input('Digite a quantidade de termos que você deseja: '))

n1 = 1
n2 = 0
n3 = 1

while quantidade != 0:
    n3 = n1 + n2
    print(f'{n1} + {n2} = {n3}')
    n1 = n2
    n2 = n3

    quantidade -= 1