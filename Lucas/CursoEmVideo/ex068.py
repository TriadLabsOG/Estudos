# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
contador = 0
from time import sleep
from random import randint
computador = randint (0, 5)
print('Olá, vamos jogar Ímpar ou Par')
sleep (2.5)
while True:
    escolha = str(input('O que você vai escolher? [Impar ou Par]? '))
    numero_jogador = int(input('Digite seu número: '))
    
    print(f'Eu joguei {computador} e você jogou {numero_jogador}')
    
    if (computador + numero_jogador) % 2 == 0 and escolha == 'Par': # Se o número for par e o jogador te escolhido par ele ganha
        print('Você ganhou. Droga, você é realmente bom!')
        contador += 1
    elif (computador + numero_jogador) % 2 == 1 and escolha == 'Impar':
        print('Você ganhou. Droga, você é realmente bom!')
        contador += 1
    else:
        break

print(f'Você perdeu. No total foram {contador} vitorias consecutivas')

