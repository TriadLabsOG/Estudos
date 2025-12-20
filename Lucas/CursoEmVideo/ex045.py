from random import randint
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
# Jogador escolhe pedra, papel ou tesoura
lista = ('pedra' , 'papel' , 'tesoura')
computador = randint (0, 2)
jogador = int(input('Qual é a sua jogada? '))
print(f'O computador escolheu {lista[computador]}')
print(f'O jogador escolheu {lista[jogador]}')
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate, tente novamente!')
    elif jogador == 1:
        print('Eu perdi, você é muito bom!')
    elif jogador == 2:
        print('Eu venci, tente novamente!')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('Eu venci, tente novamente!')
    elif jogador == 1:
        print('Empate, tente novamente!')
    elif jogador == 2:
        print('Eu perdi, você é muito bom!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('Eu perdi, você é muito bom!')
    elif jogador == 1:
        print('Eu venci, tente novamente!')
    elif jogador == 2:
        print('Empate, tente novamente!')