# Exercício Python 77: Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

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

for palavra in tupla:
    print(f'VOGAIS DE {palavra.upper()}: ', end='')
    for i in palavra:
        if i in 'aeiou':
            print(f'{i} ', end='')
    print('')
