# Exercicio 059
# Input de 2 números e MENU


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
