# Exercício Python 71: Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

# NOTAS DE 50, 20, 10, 1

# VALOR TOTAL
valor = int(input('Digite o valor a ser sacado: '))

# VARIAVEL QUE DIMINUI CONFORME AS NOTAS SÃO REMOVIDAS
notas_removidas = valor

# LISTA ACUMULADORA DE NOTAS
notas = []

# LOOP CONTADOR DE NOTAS
while True:

    # CONDIÇÃO PARA VER SE DÁ PRA PAGAR COM NOTAS DE 50
    if notas_removidas >= 50:
        notas_removidas -= 50
        notas.append(50)
    # CONDIÇÃO PARA VER SE DÁ PRA PAGAR COM NOTAS DE 20
    elif notas_removidas >= 20:
        notas_removidas -= 20
        notas.append(20)
    # CONDIÇÃO PARA VER SE DÁ PRA PAGAR COM NOTAS DE 10
    elif notas_removidas >= 10:
        notas_removidas -= 10 
        notas.append(10)
    # CONDIÇÃO PARA VER SE DÁ PRA PAGAR COM NOTAS DE 1
    elif notas_removidas >= 1:
        notas_removidas -= 1
        notas.append(1)
    # CONDIÇÃO PARA VER SE ACABOU
    if notas_removidas == 0:
        break

# RESULTADO
print(notas)