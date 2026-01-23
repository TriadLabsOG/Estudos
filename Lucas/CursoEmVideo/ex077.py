palavras = ("Amor", "Brasil", "Canto", "Dente", "Escola", "Festa", "Gato", "Homem", "Ilha", "Janela", "Livre", "Mesa", "Nuvem", "Ouro", "Porta", "Queijo", "Rua", "Sorte", "Tempo", "Vida")

for p in palavras:
    print(f'\nNas palavra {p}, temos as vogais: ', end= '')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')