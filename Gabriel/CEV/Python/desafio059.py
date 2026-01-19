# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep


numero_a = float(input('Digite um número: '))
numero_b = float(input('Digite o outro número: '))

seletor = None

while seletor != 5:
    print("""[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa""")
    seletor = int(input(''))

    # SOMA [1]
    if seletor == 1:
        resultado = numero_a + numero_b
        print(f'O resultado da soma de {numero_a} + {numero_b} é {resultado}\n')
        sleep(3)

    # MUTIPLICAÇÃO [2]
    if seletor == 2:
        resultado = numero_a * numero_b
        print(f'O resultado da multiplicação de {numero_a} + {numero_b} é {resultado}\n')
        sleep(3)

    # MAIOR [3]
    if seletor == 3:

        # IGUAIS
        if numero_a == numero_b:
            print(f'{numero_a} e {numero_b} são iguais')

        # NUMERO A MAIOR
        elif numero_a > numero_b:
            print(f'{numero_a} é maior que {numero_b}')

        #NUMERO B MAIOR
        elif numero_b > numero_a:
            print(f'{numero_b} é maior que {numero_a}')
        #
        else:
            print('Valor invalido!')
        sleep(3)

    # NOVOS NÚMEROS [4]
    if seletor == 4:
        numero_a = float(input('Digite mais um número: '))
        numero_b = float(input('Digite mais outro número: '))

print('Obrigado por utilizar a calculadora!')
sleep(3)

"""
ANTIGO

# Variavel das opções, com o valor de None ao inves de 0 (Já que vou usar o 0 em outra opção)
opcoes = None

n1 = None
n2 = None
printaropcoes = True

while opcoes != 5:
    
    # Print das opcões
    if printaropcoes == True:
        print('''[ 0 ] Somar
[ 1 ] Multiplicar
[ 2 ] Maior
[ 3 ] Novos números
[ 4 ] Exibir opções novamente
[ 5 ] Sair do programa''')
        printaropcoes = False
    
    # Input dos dois números
    if n1 == None:
        n1= int(input('Digite o primeiro número: '))
    if n2 == None:
        n2 = int(input('Digite o segundo número: '))
    
    # Input da opção
    opcoes = int(input("Digite a opção: "))
    
    # Soma [ 0 ]
    if opcoes == 0:
        print(f'{n1} + {n2} é {n1 + n2}')
     
     # Multiplicação [ 1 ]
    elif opcoes == 1:
         print(f'{n1} x {n2} é {n1 * n2}')
      
     # Maior [ 2 ]
    elif opcoes == 2:
        if n1 == n2:
            print("Os números são iguais.")
        elif n1 > n2:
            print(f'O número maior é {n1}')
        elif n2 > n1:
            print(f'O número maior é {n2}')
     
     # Novos números [ 3 ]
    elif opcoes == 3:
       n1 = None
       n2 = None
       
    # Reprintar opções [ 4 ]
    elif opcoes == 4:
        printaropcoes = True
    elif opcoes == 5:
        break
    else:
        print("ERRO: Opção invalida")
"""