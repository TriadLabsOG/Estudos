valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('-' * 30)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior número')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    print('-' * 30)
    escolha = int(input('Digite qual opção você deseja: '))

    if escolha == 1:
        soma = valor_1 + valor_2
        print(f'A soma de {valor_1} + {valor_2} equivale a {soma}')
    elif escolha == 2:
        produto = valor_1 * valor_2
        print(f'O produto entre {valor_1} e {valor_2} é igual a {produto}')
    elif escolha == 3:
        if valor_1 > valor_2:
            print(f'O número {valor_1} é maior que o {valor_2}')
        elif valor_1 < valor_2:
            print(f'O número {valor_2} é maior que o {valor_1}')
        else:
            print('Os dois valores são iguais')
    else:
        valor_1 = int(input('Digite um valor: '))
        valor_2 = int(input('Digite outro valor: '))
        