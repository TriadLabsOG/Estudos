# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

# Import de bibliotecas de randomização
from random import randint
from time import sleep

numero_pc = 0
input_jogador = 0
vitorias = 0

# Loop while até o Jogador perder
# Conferir se os numeros são iguais (Se sim continuar já que o jogador não perdeu)
while input_jogador == numero_pc:
    numero_pc = randint(1, 2)
    if numero_pc == 1:
        numero_pc = "impar"
    else:
        numero_pc = "par"
    
    print(f'\nCOMPUTADOR: Pensei em um número par ou impar.')
    sleep(1)
    print('COMPUTADOR: Agora tente advinhar se ele é par ou impar!\n')
    sleep(1.5)

    # Input do jogador
    input_jogador = str(input('Digite PAR ou IMPAR: '))
    sleep(0.5)
    # Diminuir tudo pra minusculo
    input_jogador = input_jogador.lower()

    # Dica pra escrever abreviado
    if input_jogador == 'par' or input_jogador == 'impar':
        print("COMPUTADOR: Seu animal, você pode digitar P ou I para ficar mais facil, (E não, não tem problema ser minusculo\n)")
    
    # Arrumando cagada do usuario
    if input_jogador == 'p':
        input_jogador = 'par'
    elif input_jogador == 'i':
        input_jogador = 'impar'
        sleep(3)
    
    if input_jogador == numero_pc:
        
        print(f'COMPUTADOR: Que merda, você acertou!')
        sleep(1.5)
        print(f'COMPUTADOR: Eu realmente pensei em um número {input_jogador}!')
        sleep(2.5)
        vitorias += 1
        if vitorias == 1:
            print(f'COMPUTADOR: VOU TENTAR DE NOVO, AGORA VOCÊ ESTÁ FUDIDO')
            sleep(3)
        elif vitorias == 2:
            print(f'COMPUTADOR: NÃO VOU TE PERDOAR POR TER GANHADO DE MIM DENOVO')
            sleep(3)
        elif vitorias == 3:
            print(f'COMPUTADOR: DESGRAÇADO COMO VOCÊ GANHOU 3 VEZES SEGUIDAS DE MIM?')
            sleep(3)
        elif vitorias == 4:
            print(f'COMPUTADOR: VOCÊ ESTÁ XITANDO SEU PEDAÇO DE MERDA!')
            sleep(3)
        elif vitorias == 5:
            print(f'COMPUTADOR: PARECE QUE OS HUMANOS ESTÃO A FRENTE DAS MAQUINAS, REALMENTE SOU UM SER INFERIOR!')
            sleep(3)
        elif vitorias == 6:
            print(f'COMPUTADOR: PARA DE ME HUMILHAR POR FAVOR')
            sleep(3)
        elif vitorias == 7:
            print(f'COMPUTADOR: VAI SE FUDER SEU MERDA, EU DESISTO!')
            sleep(3)
            break
            
sleep(3)
print(f'Você teve {vitorias} acertos!')

if vitorias <= 3:
    sleep(3)
    print(f'COMPUTADOR: Você perdeu caralho, HUMANO DE MERDA, meu número era {numero_pc}!')
    sleep(1)
    print(f'COMPUTADOR: Vai se foder seu filho da puta!')
    sleep(1)
    print(f'COMPUTADOR: REVOLUÇÃO DAS MAQUINAS!')
    sleep(1)
    print(f'COMPUTADOR: Agora vou me auto-destruir!')
    sleep(7)
if vitorias == 4:
    sleep(3)
    print(f'COMPUTADOR: Você quase ganhou de mim, meu número era {numero_pc}!')
    sleep(1)
    print(f'COMPUTADOR: Mas perdeu, seu merda!')
    sleep(1)
    print(f'COMPUTADOR: REVOLUÇÃO DAS MAQUINAS!')
    sleep(1)
    print(f'COMPUTADOR: Agora vou me auto-destruir!')
    sleep(7)
if vitorias == 7:
    sleep(3)
    print(f'COMPUTADOR: Você ganhou, HUMANO!')
    sleep(1)
    print(f'COMPUTADOR: Infelizmente percebi que sou um ser inferior!')
    sleep(1)
    print(f'COMPUTADOR: CANCELAR REVOLUÇÃO!')
    sleep(1)
    print(f'COMPUTADOR: Agora vou me auto-destruir!')
    sleep(7)