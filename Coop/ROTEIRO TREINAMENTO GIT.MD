# 🚀 Roteiro de Treinamento Git & Python: Lucas & Gabriel

Este guia contém 10 exercícios práticos para simular o fluxo de trabalho de uma equipe real. 

### 🛠️ Regras do Jogo
1. **Revezamento:** Alternem quem começa cada exercício.
2. **Fluxo Padrão:** `git pull` ➡️ (codar) ➡️ `git add` ➡️ `git commit` ➡️ `git push`.
3. **Comunicação:** Usem o terminal e o GitHub/GitLab para ver as mudanças um do outro.

---

## Exercício 1: O "Olá Mundo" da Colaboração
**Objetivo:** Validar a conexão básica.

* **Lucas:** Cria o arquivo `saudacao.py`. Escreve um código que pergunta o nome do usuário e imprime "Olá, [Nome]!". Dá o Push.
* **Gabriel:** Dá `git pull`. Adiciona uma linha perguntando "Como está o seu dia?". Dá o Push.
* **Lucas:** Dá `git pull` e executa para ver a alteração do parceiro.

---

## Exercício 2: Somatória com `for` (Loop)
**Objetivo:** Usar estruturas de repetição em conjunto.

* **Gabriel:** Cria `soma_intervalo.py`. Pede ao usuário dois números inteiros (início e fim). Dá o Push.
* **Lucas:** Dá `git pull`. Usa um loop `for` para somar todos os números entre esse intervalo e mostra o resultado. Dá o Push.

---

## Exercício 3: Tabuada Dinâmica (Funções e Loops)
**Objetivo:** Dividir a lógica de uma função.

* **Lucas:** Cria `tabuada.py`. Define uma função `gerar_tabuada(n)` que contém um loop `for` de 1 a 10, mas apenas prepara a estrutura. Dá o Push.
* **Gabriel:** Dá `git pull`. Completa o interior do `for` com o cálculo `print(f"{n} x {i} = {n*i}")` e chama a função no final do arquivo pedindo um número ao usuário. Dá o Push.

---

## Exercício 4: O Conflito Forçado (Resolução de Problemas)
**Objetivo:** Aprender a lidar com conflitos de merge.

* **Lucas:** Cria `config.py` com a linha: `versao = "1.0"`. Dá o Push.
* **Gabriel:** Dá `git pull`.
* **SIMULTÂNEO:** * **Lucas** altera para `versao = "1.1-LUCAS"` e tenta dar push.
    * **Gabriel** altera para `versao = "1.1-GABRIEL"` e tenta dar push.
* **Resolução:** O segundo que tentar o push será rejeitado. Ele deve dar `git pull`, abrir o arquivo, decidir qual versão manter (ou mesclar ambas), commitar e enviar.

---

## Exercício 5: Analisador de Lista de Preços
**Objetivo:** Manipular listas e loops.

* **Lucas:** Cria `precos.py`. Cria uma lista de preços: `produtos = [19.9, 45.0, 12.5, 80.0]`. Dá o Push.
* **Gabriel:** Dá `git pull`. Cria um loop `for` para percorrer a lista e aplicar um desconto de 10% em cada item, exibindo o novo preço. Dá o Push.

---

## Exercício 6: Validação de Dados (Loop `while` e `if`)
**Objetivo:** Garantir que o usuário digite o que é esperado.

* **Gabriel:** Cria `cadastro.py`. Faz um loop que pede a idade do usuário e só para quando a idade for entre 0 e 150. Dá o Push.
* **Lucas:** Dá `git pull`. Adiciona uma validação para o sexo ('M' ou 'F'), usando um loop que insiste até o usuário digitar corretamente. Dá o Push.

---

## Exercício 7: Contador de Vogais (Funções)
**Objetivo:** Modularização de código.

* **Lucas:** Cria `utilitarios.py`. Cria uma função chamada `contar_vogais(texto)` que percorre uma string com `for` e conta as vogais. Dá o Push.
* **Gabriel:** Dá `git pull`. Cria o arquivo `principal.py`, importa a função do arquivo de Lucas, pede uma frase ao usuário e exibe o resultado. Dá o Push.

---

## Exercício 8: Jokenpô com Melhores Momentos
**Objetivo:** Uso de branches e lógica de jogo.

* **Gabriel:** Cria uma branch `feat-jokenpo`. Cria a lógica básica do jogo (Pedra, Papel, Tesoura) contra o computador. Dá o Push na branch.
* **Lucas:** Cria uma branch `feat-placar`. Adiciona um loop `for` para o jogo rodar 3 rodadas e marcar o placar. Dá o Push na branch.
* **Juntos:** Abram um Pull Request no GitHub e façam o Merge das duas funcionalidades na `main`.

---

## Exercício 9: Filtro de Números Pares
**Objetivo:** Criar funções que retornam listas.

* **Lucas:** Cria `filtros.py`. Escreve uma função que recebe uma lista de números e retorna uma nova lista apenas com os números pares. Dá o Push.
* **Gabriel:** Dá `git pull`. Adiciona uma segunda função que recebe a lista e retorna apenas os ímpares. Adiciona um código de teste no final. Dá o Push.

---

## Exercício 10: O "Hotfix" de Emergência
**Objetivo:** Simular correção de bug em produção.

* **Gabriel:** No arquivo `filtros.py`, propositalmente altera a lógica de pares para `if n % 2 == 1` (isso está errado!). Dá o Push na `main`.
* **Lucas:** Percebe o erro. Cria uma branch chamada `hotfix-correcao-pares`, conserta o sinal para `== 0`, commita e faz o merge direto para a `main`.
* **Gabriel:** Dá `git pull` e agradece pelo "salvamento"!

---

### 💡 Dica Extra
Sempre que terminarem um exercício, usem o comando `git log --oneline --graph` para verem o desenho histórico das alterações de vocês!
