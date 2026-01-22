# Desafio 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
PRIMEIRO_TERMO = int(input('Digite o primeiro termo da P.A: '))
RAZAO = int(input('Digite a razão da P.A: '))
quantidade_de_termos = 10

termo = PRIMEIRO_TERMO

while termo != (PRIMEIRO_TERMO + RAZAO * quantidade_de_termos):
    print(f'{termo} > ', end='')
    termo += RAZAO
    if termo == (PRIMEIRO_TERMO + RAZAO * quantidade_de_termos):
        print('FIM')
        print('\nDigite mais quantos termos quer ver.')
        quantidade_de_termos += int(input('DIGITE "0" SE NÃO FOR NENHUM: '))

"""
ANTIGO

# Input do primeiro termo e da razão pra poder fazer os calculos.
primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

# Quantidade de termos que vai começar na P.A 
# 9 porque já vai mostrar o primeiro_termo no print (Ou sejá, vai printar 10)
quantidade_de_termos_iniciais = 9

# Print do primeiro termo pra ele aparecer antes dos outros
print(f'{primeiro_termo} > ', end='')

# Quantidade de termos mostrados (Começa com 1 porque já vai mostrar o primeiro_termo)
termos = 1

# Loop da quantidade de termos iniciais até chegar a 0
while quantidade_de_termos_iniciais != 0:
    termos += 1
    # Somando o primeiro termo com a razão, pra sempre aumentar o valor da razão.
    primeiro_termo += razão
    # Printando o primeiro termo sempre com o adicional da razão em loop
    print(f'{primeiro_termo}  > ', end='')
    # Diminuindo a quantidade de termos iniciais pra chegar a 1 e parar o loop
    quantidade_de_termos_iniciais -= 1
    if quantidade_de_termos_iniciais == 0:
        print('PAUSA')
        quantidade_de_termos_iniciais = int(input('\nVocê quer mais quantos termos: '))

# Quantidade de termos mostrados (Autoexplicativo kkk)
print(f'Quantidade de termos mostrados: {termos}')
"""