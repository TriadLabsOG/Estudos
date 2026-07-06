# Aula 1- Seja um Programador: -

# Aula 2- Para que serve o Python?: -

# Aula 3- Instalando o Python3 e o IDLE: -

# Aula 4- Primeiros comandos em Python3:
	print( ): **Escreve o que o usuário definir dentro do parênteses no terminal** 

	' ':  Define as strings e é usado no print para colocar uma mensagem no terminal

	Variáveis: São definidas por um nome  qualquer **SEMPRE EM MINUSCULO**(exemplo: nome) e tem um sinal de igual para definir o valor dessa variável(exemplo: nome = Lucas, peso = 65kg, idade = 15). Podendo chamar com a função print(Exemplo: print(nome, idade, peso))

	input: é o comando que permite o usuário a escrever no terminal, armazenando dentro de uma variável(Exemplo: nome= input('Qual é o seu nome? ))

# Aula 5 – Instalando o PyCharm e o QPython3: -

# Aula 6 – Tipos Primitivos e Saída de Dados: 

	int( : Tudo que esta dentro do parênteses é convertido em números inteiros(Exemplo: n1 = int(input('Digite um número: ')))

	str( : Tudo que está dentro do parênteses é convertido em strings(Exemplo: nome = str(input('Qual é o seu nome? ')))

	float( : Tudo que esta dentro do parênteses é convertido em números quebrados(1.1), sempre apresentando um ponto(.) no meio dos números para indicar um número flutuante, nunca apresentando uma virgula(Exemplo: peso = float(input('Qual é o seu peso? ')))

	bool( : Tudo que está dentro do parênteses é convertido como verdadeiro(True) ou falso(False)
	(Observação: sempre que for representar True ou False, a primeira letra sempre tem que ser maiúscula)

	type(): Coloca no terminal o tipo primitivo da variável

	.isnumeric: Da a informação se a variável é um número(sempre dando True ou False no terminal)

	.isalnum: Da a informação se a variável é um número ou uma letra alfabética(sempre dando True ou False no terminal)

	.isupper: Da a informação se a string está toda em letra maiúscula(sempre dando True ou False no terminal)

# Aula 7 – Operadores Aritméticos:
	+(Adição)
	-(Subtração)
	*(Multiplicação)
	/(Divisão)
	**(Potencia)
	//(Divisão inteira
	%(Modulo/ Resto da divisão inteira)

	Ordem de Precendencia:
	1º: ()
	2º: **
	3º: *, /, //, %
	4º: +, -


# Aula 8 – Utilizando Módulos:
	import : Importa uma biblioteca com todas suas funções
	from (biblioteca) import (função): Importa uma função unica de uma biblioteca

	As bibliotecas mais utilizadas são:
	math(importa os recursos da matematica):
		ceil: arredonda um número para cima(0.5 -> 1)
		floor: arredonda um número para baixo(1.3 -> 1)
		trunc: elimina a virgula(2.5 -> 2)
		pow: faz a potencia(3**2 == 9)
		sqrt: faz a raiz quadrada(numero ** 0.5)
		factorial: faz o fatorial do numero(3! == 3 * 2 * 1 == 6)
	random(importa os recursos de randomização):
		randint(x, y): escolhe um numero inteiro aleatorio que o usuario colocar
		

# Aula 9 – Manipulando Texto:
	Fatiamento: Fatia a frase/string. Exemplos de fatiamentos:
		frase[x]: Pega apenas a letra que esta na posição(x) que esta entre colchetes
		frase[x:y]: Pega a letra que esta na posição(x) e vai até a posição y, excluindo o extremo(y)
		frase[x:y:z]: Pega a letra que esta na posição(x) e vai até a posição y, excluindo o extremo(y) mas pulando de numero em numero(z)
		frase[:x]: Ele começa do caractere 0 até a letra que esta na posição(x), excluindo o extremo(x)
		frase[x:]: Ele começa da posição(x) até o final, incluindo o extremo
		frase[x::y]: Começa da posição(x) até o final, pulando de número em número(y)
	
	Analise: Analisa a frase. Exemplos de analises:
		len(frase): Le a quantidade de caracteres da frase
		frase.count('x'): Conta quantas letras(x) tem na frase
		frase.count('x', y, z): Ele conta da posição(y) até a posição(z) quantas letras(x) tem
		frase.find('x'): Conta quantas vezes achou tal string(x). Se você colocar uma string que não existe, irá retornar o valor -1
	'x' in frase: Devolve em True ou False se tem a str na frase
	
	Transformação: Tranforma a frase, podendo adicionar, tirar ou substituir strings. Exemplos de tranformação:
		frase.replace('x', 'y'): Transforma a str x para y
		frase.upper(): Deixa todas as strings em letras maiuscula
		frase.lower(): Deixa todas as strings em letras minusculas
		frase.capitalize(): Deixa todas as primeiras letras em maiuscula
		frase.title(): Conta quantas palavras tem na frase e da um capitalize
		frase.strip(): Remove todos os espaços inuteis da string
		frase.rstrip(): Remove todos os espaços inuteis da direita da string
		frase.lstrip(): Remove todos os espaços inuteis da esquerda da string
		
	Divisão: Divide string. Exemplos de divisões:
		frase.split(): Divide as frases de acordo com seus espaços, dando novos valores para as strings(criando uma lista)
		'-'join(frase): Junta todos os elementos da frase e vai separar so com um espaço para cada elemento
		
		
# Aula 10 – Condições (Parte 1):
	if: Condição de "se" algum evento acontece(if nota < 6: )
	
	else: Condição de "se não" algum evento acontece(else: )
	Todo comando que esta com identação, vai acontecer com base no if ou else. Todos que estiverem a esquerda vão acontecer sempre

	