# Palindromo

palavra = str(input('Digite uma palavra: '))

#Diferenciação maiuscula e espaços

palavra_com_diferenciacao = palavra.replace(" ","").upper()

# Lista de divisão das letras da palavra
lista_div_das_letras = []
for i in range(0, len(palavra_com_diferenciacao)):
    lista_div_das_letras.append(palavra_com_diferenciacao[i])


# Lista com o index da outra lista invertido, assim dando pra testar se é palindromo, caso seja igual
lista_invertida = []
for i in range(0, len(palavra_com_diferenciacao)):
    # Adicionando a palavra com o indice invertido usando o simbolo de negativo, porem preciso somar -1 porque se não começa do 0 (O que no caso não seria  a ultima letra e sim a primeira letra da lista.)
    lista_invertida.append(palavra_com_diferenciacao[-i -1])
print('teste: ',lista_invertida)
# Teste condicional de comparação entre as variaveis de lista
if lista_div_das_letras == lista_invertida:
    print(f'A palavra "{palavra}" é palindromo')
elif lista_div_das_letras != lista_invertida: 
    print(f'A palavra "{palavra}" não é palindromo')
