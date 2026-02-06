tupla = ('Coca-Cola 2L', 15.99 ,
         'Arroz Camil KG', 20.49,
         'Monitor 999Hz', 10000,
         'Feijão Camil', 6.99,
         'Bobbie Goods', 40.99,
         'Bola Copa Do Mundo 2026', 200,
         'Camisa Do Palmeiras', 250.99
)

print('-=-' * 30)
for pos in range(0 , len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]}', end= ' ')
    else:
        print(f'R${tupla[pos]}')

print('-=-' * 30)