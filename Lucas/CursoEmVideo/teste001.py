print("Digite valores para adicionar à lista: ")
lista_dinamica = []
while True:
    entrada = input("Valor: ")
    if entrada == "": # Se o usuário não digitar nada e apertar Enter
        break # Sai do loop
    lista_dinamica.append(entrada) # Adiciona o valor digitado

print("Sua lista final:", lista_dinamica)
