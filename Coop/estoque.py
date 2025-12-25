# 2. Estoque Simples

# Gabriel: Na main (após Pull), crie a branch feat-estoque. Em estoque.py, crie um dicionário {produto: preco} e um for que imprime produtos caros (> 50). Commit, Push e PR.

# Lucas: Aceite o PR. Na main (após Pull), crie a branch feat-busca. Adicione uma função que recebe o nome de um produto e diz se ele está no estoque. Commit, Push e PR.

produtos_varejo = [
    {
        'id': '1',
        'produto': 'Coca-Cola 600ml',
        'valor': 5.00,
        'estoque': 81
    },
    {
        'id': '2',
        'produto': 'Arroz 5kg',
        'valor': 30.00,
        'estoque': 23
    },
    {
        'id': '3',
        'produto': 'Feijão 1kg',
        'valor': 8.50,
        'estoque': 76
    },
    {
        'id': '4',
        'produto': 'Açucar 5kg',
        'valor': 19.25,
        'estoque': 20
    },
    {
        'id': '5',
        'produto': 'Azeite 500ml',
        'valor': 52.90,
        'estoque': 10
    },
    {
        'id': '6',
        'produto': 'Picanha 1kg',
        'valor': 89.99,
        'estoque': 90
    },
    {
        'id': '7',
        'produto': 'Ventilador',
        'valor': 200.00,
        'estoque': 0
    },
    {
        'id': '8',
        'produto': 'Jogo de Taças Cristal',
        'valor': 55.00,
        'estoque': 20
    },
    {
        'id': '9',
        'produto': 'Coca-Cola 2L',
        'valor': 11.90,
        'estoque': 10
    }
]

for produto in produtos_varejo:
    if produtos_varejo[produto] > 50:
        print(f'{produto}: {produtos_varejo[produto]}')

def buscador_de_produtos(lista_produtos, produto_procurado):
    
    for produto in lista_produtos:
        if produto == produto_procurado:
            return True
    return False


    
print(buscador_de_produtos(produtos_varejo, 'Picanha'))

