valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))
escolha = 0
while escolha < 5:
    print('-'* 20)
    print('Qual opção você ira escolher')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    print('-' * 20)
    escolha = int(input('Digite a opção a seguir: '))

    if escolha == 1:
        print(f'{valor_1} + {valor_2} = {valor_1 + valor_2}')
    elif escolha == 2:
        print(f'{valor_1} x {valor_2} = {valor_1 * valor_2}')
    elif escolha == 3:
        if valor_1 > valor_2:
            print(f'O número {valor_1} é o maior')
        elif valor_2 > valor_1:
            print(f'O número {valor_2} é o maior')
        else:
            print('Os dois valores são os mesmos')
    else:
        valor_1 = int(input('Digite um valor: '))
        valor_2 = int(input('Digite outro valor: '))
        escolha = int(input('Digite a opção a seguir: '))
    
