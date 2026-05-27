# Exercício Python 73: Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

colocados = (
    "Botafogo",
    "Chapecoense",
    "EC Vitória",
    "Fluminense",
    "Mirassol",
    "Bahia",
    "São Paulo",
    "Athletico-PR",
    "Bragantino",
    "Palmeiras",
    "Atlético-MG",
    "Flamengo",
    "Grêmio",
    "Corinthians",
    "Vasco da Gama",
    "Coritiba",
    "Internacional",
    "Santos",
    "Remo",
    "Cruzeiro",
)

# 20 primeiros em ordem
print(colocados)

# 5 primeiros
print(colocados[0:5])

# 4 ultimos
print(colocados[-4 : len(colocados) + 1])

# em ordem alfabetica
print(sorted(colocados))

# Posição do Chapecoense
posicao_chapecoense = "Fora da tabela!"
ordem_colocacao_loop = 0

for colocado in colocados:
    ordem_colocacao_loop += 1
    if colocado == "Chapecoense":
        posicao_chapecoense = ordem_colocacao_loop
        print(f"O Chapecoense é o {posicao_chapecoense}º colocado no Brasileirão.")
        break
if posicao_chapecoense == "Fora da tabela!":
    print(f"O Chapecoense está fora da tabela!")
