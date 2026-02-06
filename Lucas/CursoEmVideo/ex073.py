times = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG','Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'America-MG', 'Sport', 'Vitória', 'Paraná'
# Essa é a classificação do Brasileirão de 2018(que meu Palmeiras ganhou)
print(f'Os cinco primeiros classificados foram {times[0:5]}')
print('-=-' * 20)
print(f'Os quatro ultimos times foram {times[16:20]}')
print('-=-' * 20)
print(f'Os times em ordem alfabetica ficam assim {sorted(times)}')
print('-=-' * 20)
print(f'A Chapecoense ficou na {times.index('Chapecoense')}ª posição')