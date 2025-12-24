# Lucas: Na main, crie a branch feat-media. Em notas.py, crie uma função que recebe uma lista e retorna a média. Commit: feat: add calculo de media. Push e abra PR.

# Gabriel: Aceite o PR. No VS Code, mude para main, dê Pull. Crie a branch feat-validacao. No arquivo, use um if para validar se a nota está entre 0 e 10. Commit: fix: valida intervalo de notas. Push e PR.


def media(lista):   
    ''' 
    A função calcula a media de uma lista.

    Args: 
        lista(list): int e float

    Returns:
        float: Media dos valores da lista

    Raises:
        ValueError: Se a lista estiver vazia
    '''
    if lista == []:
        raise ValueError('Nenhuma nota entre 0 e 10 encontrada na lista')
    return sum(lista) / len(lista)

lista_notas = [10, 20, 30, 2, 3, 4, 1.2]
lista_notas_pequenas = []
for nota in lista_notas:
    if nota >= 0 and nota <= 10:
        lista_notas_pequenas.append(nota)

print(media(lista_notas_pequenas))
