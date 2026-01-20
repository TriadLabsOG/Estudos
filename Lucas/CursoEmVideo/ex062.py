# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0 # O contador de quantos numeros apareceram
total_termos = 0 # Começamos com nenhum
mais_termos = 10 # Inicialmente começamos com 10 termos na P.A

while mais_termos != 0:  # Enquanto o usuario não digitar zero, calculamos a P.A
    total_termos += mais_termos

    while contador <= total_termos:
        print(f'{termo} -> ', end= '')
        termo += razao # Enquanto o contador não chegar em 10, calculamos a P.A
        contador += 1 # Sempre que fazemos o termo + razão, adicionamos um número ao contador

    print('PAUSA') # Ira pausar a exibicção dos numeros quando chegar em 10

    mais_termos = int(input('Quantos termos você quer adicionar a mais? ')) # Se o usuario digitar um valor diferente do que 0, o programa ira voltar ao primeiro while

print(f'Fim da progressão aritimetica com {total_termos} termos exibidos') # Quando o usuario digitar 0, ira mostrar esse print com o tanto de termos exibidos

