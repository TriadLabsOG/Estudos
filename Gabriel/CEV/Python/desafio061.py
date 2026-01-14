"""
ANTIGO

# Input do primeiro termo e da razão pra poder fazer os calculos.
primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

# Quantidade de termos que vai começar na P.A
quantidade_de_termos_iniciais = 10

# Print do primeiro termo pra ele aparecer antes dos outros
print(f'{primeiro_termo} > ', end='')

# Loop da quantidade de termos iniciais até chegar a 1
# Porque se não vai mostrar 10 termos, e a gente quer que o primeiro_termo fique no inicio, assim dando 10 termos.
while quantidade_de_termos_iniciais != 1:
    primeiro_termo += razão
    print(f'{primeiro_termo}  > ', end='')
    quantidade_de_termos_iniciais -= 1 
print('Fim')
"""