# Exercício Python 77: Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# TUPLA COM OS ITENS
tupla = (
        "ovo",
        "salada",
        "tropeiro",
        "frango",
        "peixe",
        "sushi",
        "abacaxi",
        "abobora"
        )

# LOOP PALAVRA POR PALAVRA E ADICIONANDO NO PRINT
for palavra in tupla:
    print(f'VOGAIS DE {palavra.upper()}: ', end='')

    # LOOP LETRA POR LETRA CONFERINDO SE TEM VOGAIS COM UM IF
    for i in palavra:
        if i in 'aeiou':
            print(f'{i} ', end='')

    # ATALHO PARA QUEBRAR LINHA
    print('')
