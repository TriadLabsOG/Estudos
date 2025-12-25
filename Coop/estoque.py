# 2. Estoque Simples

# Gabriel: Na main (após Pull), crie a branch feat-estoque. Em estoque.py, crie um dicionário {produto: preco} e um for que imprime produtos caros (> 50). Commit, Push e PR.

# Lucas: Aceite o PR. Na main (após Pull), crie a branch feat-busca. Adicione uma função que recebe o nome de um produto e diz se ele está no estoque. Commit, Push e PR.

produtos_varejo = {
    'Coca-Cola 600ml': 5.00,
    'Arroz 5kg': 30.00,
    'Feijão 1kg': 8.50,
    'Açucar 5kg': 19.25,
    'Azeite 500ml': 52.90,
    'Picanha 1kg': 89.99,
    'Ventilador': 200.00,
    'Jogo de Taças Cristal': 55.00,
    'Coca-Cola 2L': 11.90
}

print('PRODUTOS MAIS CAROS QUE 50 REAIS')
for produto in produtos_varejo:
    if produtos_varejo[produto] > 50:
        print(f'{produto}: {produtos_varejo[produto]}')