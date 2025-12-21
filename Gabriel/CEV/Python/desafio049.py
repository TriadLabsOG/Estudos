#TABUADA

num = int(input('Número da tabuada: '))

print(f'\nTABUADA DO {num}')
for i in range(1, 11):
    print(f"{num} x {i:2} = {num * i}")