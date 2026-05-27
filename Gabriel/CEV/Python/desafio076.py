# Exercício Python 76: Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = (
    "Prato",
    10.00,
    "Vassoura",
    15.00,
    "Peixe",
    30.00,
    "Caderno",
    12.00,
    "Chinelo",
    35.00,
    "Macbook",
    9123.23,
)

print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
for i in range(0, len(tupla)):
    if i == 0 or i % 2 == 0:
        print(f"{tupla[i]:.<30}R$ ", end="")
    else:
        print(f"{tupla[i]:>7.2f}")
print("-" * 40)
