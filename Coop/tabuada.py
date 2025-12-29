'''3. Tabuada com Histórico
Lucas: Crie a branch feat-tabuada. Em tabuada.py, use um for para gerar a tabuada de um número e salve os resultados em uma lista com .append(). Commit, Push e PR.
Gabriel: Aceite o PR. Na main (após Pull), crie a branch feat-loop. Envolva o código em um while True para repetir o processo até o usuário mandar parar. Commit, Push e PR.'''

numero_para_tabuada = 8
numeros_da_tabuada = []

for t in range(1, 11):
    tabuada = numero_para_tabuada * t
    numeros_da_tabuada.append(tabuada)

