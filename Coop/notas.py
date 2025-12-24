''' 1. Média Acadêmica
 * **Lucas:** Na `main`, crie a branch `feat-media`. Em `notas.py`, crie uma função que recebe uma lista e retorna a média. `Commit: feat: add calculo de media`. Push e abra PR.
* **Gabriel:** Aceite o PR. No VS Code, mude para `main`, dê **Pull**. Crie a branch `feat-validacao`. No arquivo, use um `if` para validar se a nota está entre 0 e 10. `Commit: fix: valida intervalo de notas`. Push e PR.'''


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
        raise ValueError('A lista não pode estar vazia')
    return sum(lista) / len(lista)


