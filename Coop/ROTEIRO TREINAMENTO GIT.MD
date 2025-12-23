# 🎓 Masterclass Git & Python: Fluxo de Trabalho Lucas & Gabriel

Este roteiro utiliza o **GitHub Flow**, o padrão ouro em empresas de tecnologia. Vamos usar exclusivamente a interface visual do VS Code para gerenciar o código.

---

## 🛠️ O Coração do VS Code: O Controle de Código-Fonte
Antes de começar, localize o ícone de **"Controle do Código-Fonte"** (parece um grafo com três círculos) na barra lateral esquerda. É aqui que a mágica acontece.

### Os Conceitos Fundamentais que você vai usar:
1.  **Branches (Ramificações):** No mundo real, a `main` é o código que está rodando para o cliente. Criamos uma branch para trabalhar isolados, como uma cópia de rascunho, para não "quebrar" o sistema principal.
2.  **Sincronizar (Pull):** É como atualizar o seu "feed". Antes de começar qualquer tarefa, você traz as novidades que o seu colega enviou para a nuvem.
3.  **Stage (+):** É o ato de "preparar" o arquivo. Você avisa ao Git quais alterações devem entrar na próxima "foto" (commit) do projeto.
4.  **Commit:** É a "foto oficial" ou o "save" do código. Você dá um nome (mensagem) a essa versão para poder rastrear o progresso ou desfazer erros.
5.  **Push (Publicar):** É enviar seus commits da sua máquina para o servidor do GitHub.
6.  **Pull Request (PR):** É um pedido de revisão. Você avisa seu colega que terminou algo e pede para ele aprovar a união do seu rascunho com o código principal.

---

## Exercício 1: Médias Acadêmicas (Lucas começa)
**Foco:** Funções, Loops `for` e Revisão por Pares.

**Passo a Passo:**
1. **Lucas:** No canto inferior esquerdo do VS Code, clique em `main` e selecione **"Criar nova ramificação"**. Nomeie como `feat-media`.
2. **Lucas:** Crie o arquivo `notas.py`. Escreva uma função que recebe uma lista de notas, usa um loop `for` para somá-las e retorna a média.
3. **Lucas:** No ícone do Git, clique no **+** ao lado do arquivo (Stage), digite a mensagem `feat: adiciona calculo de media` e clique no botão de **Confirmar (Commit)**.
4. **Lucas:** Clique em **"Publicar Ramificação"**. Vá ao GitHub no navegador e clique no botão verde **"Compare & pull request"** para enviar para o Gabriel.
5. **Gabriel:** No GitHub, vá na aba "Pull Requests", clique no PR do Lucas, olhe o código em "Files Changed" e, se estiver tudo certo, clique em **"Merge Pull Request"**.
6. **Gabriel:** No VS Code, mude para a branch `main`, clique em **Sincronizar (Pull)**. Agora, crie a sua branch `feat-validacao`.
7. **Gabriel:** No arquivo `notas.py`, adicione um loop `while` que impede o usuário de digitar notas menores que 0 ou maiores que 10. Repita o processo de Commit, Push e abra o PR para o Lucas.

---

## Exercício 2: Analisador de Estoque (Gabriel começa)
**Foco:** Dicionários e filtragem com `for`.

**Passo a Passo:**
1. **Gabriel:** Crie a branch `feat-estoque`. Crie `estoque.py` com um dicionário `{produto: preco}`. Use um `for` com `.items()` para imprimir apenas produtos caros (ex: > R$ 50).
2. **Gabriel:** Faça o Commit e Push. Abra o PR. O objetivo é isolar a lógica de listagem da lógica de busca.
3. **Lucas:** Após aceitar o PR no GitHub, volte para a `main` no VS Code e dê **Pull**. Crie a branch `feat-busca`.
4. **Lucas:** Crie uma função que recebe um nome de produto. Use o operador `if item in estoque` para verificar a existência. 
5. **Lucas:** Envie o PR. Trabalhar em branches diferentes garante que, se a "busca" falhar, a "listagem" do Gabriel continue funcionando na `main`.

---

## Exercício 3: Tabuada com Histórico (Lucas começa)
**Foco:** Métodos de lista (`.append`) e loops `while` de controle.

**Passo a Passo:**
1. **Lucas:** Crie a branch `feat-tabuada`. No arquivo `tabuada.py`, use um `for` de 1 a 10 e guarde cada resultado em uma lista vazia usando o comando `.append()`. 
2. **Lucas:** Faça o Commit, Push e PR.
3. **Gabriel:** Aceite o PR, dê **Pull** na `main` e crie a branch `feat-loop-infinito`.
4. **Gabriel:** Envolva o código em um `while True`. Isso permite que o usuário calcule várias tabuadas seguidas. Ao final, use um `for` para imprimir o histórico de todas as listas geradas. Envie o PR.

---

## Exercício 4: O Conflito Visual (Simultâneo)
**Foco:** Resolução de conflitos de edição na mesma linha pelo VS Code.

**Passo a Passo:**
1. **Preparação:** Lucas cria `config.py` com `BANCO = "SQLite"`, faz commit e push direto na `main`. Ambos dão **Pull**.
2. **Lucas:** Na branch `ajuste-lucas`, muda o texto para `"PostgreSQL"`. Faz commit.
3. **Gabriel:** Na branch `ajuste-gabriel`, muda o texto para `"MySQL"`. Faz commit e faz o Merge no GitHub primeiro.
4. **O Conflito:** Lucas tenta fazer o Merge no GitHub e recebe o aviso de **"Conflict"**.
5. **Resolução:** No VS Code, Lucas muda para a `main`, dá **Pull** (recebe o "MySQL" do Gabriel). Lucas volta para sua branch `ajuste-lucas` e clica em **"Mesclar de... main"**.
6. **VS Code:** O arquivo abrirá com marcações coloridas. Clique nas opções que aparecem acima do código: **"Aceitar Atual"**, **"Aceitar Entrada"** ou **"Aceitar Ambas"**. Escolha uma, salve, clique no **+** (Stage) e faça um commit de correção.

---

## Exercício 5: Validador de Senhas (Gabriel começa)
**Foco:** Strings como listas e loops de inspeção.

**Passo a Passo:**
1. **Gabriel:** Branch `feat-senha-base`. No arquivo `seguranca.py`, use `for char in senha` para verificar se a string tem mais de 8 caracteres. PR enviado.
2. **Lucas:** Aceite, dê **Pull** na `main` e crie a branch `feat-seguranca-extra`.
3. **Lucas:** Dentro do `for` criado pelo Gabriel, use o método `.isdigit()` para verificar se existe algum número na senha. Se não houver, avise que a senha é fraca. Isso simula uma melhoria de requisito de segurança.

---

## Exercício 6: Simulador de Financiamento (Lucas começa)
**Foco:** Lógica matemática e acumuladores.

**Passo a Passo:**
1. **Lucas:** Branch `feat-calc`. Em `financiamento.py`, peça o valor total e o salário. Calcule a parcela simples. PR enviado.
2. **Gabriel:** Aceite, dê **Pull** na `main` e crie a branch `feat-tabela`.
3. **Gabriel:** Use um loop `for` que itera 12 vezes. Em cada iteração, mostre o saldo devedor diminuindo. Isso ensina como loops geram projeções de dados.

---

## Exercício 7: Sorteio de Grupos (Gabriel começa)
**Foco:** `import random` e fatiamento de listas.

**Passo a Passo:**
1. **Gabriel:** Branch `feat-random`. Importe a biblioteca `random`. Crie uma lista de nomes e use `random.shuffle(lista)`. PR enviado.
2. **Lucas:** Aceite, dê **Pull** e crie a branch `feat-duplas`.
3. **Lucas:** Use um loop `for` com `range(0, len(lista), 2)`. Isso permite que você acesse a lista de 2 em 2 para imprimir os nomes como duplas formadas.

---

## Exercício 8: Contador de Caracteres (Lucas começa)
**Foco:** Contadores manuais dentro de loops.

**Passo a Passo:**
1. **Lucas:** Branch `feat-contagem`. Em `texto.py`, use um `for` para percorrer uma frase digitada e incremente uma variável `contador` toda vez que encontrar um espaço `" "`. PR enviado.
2. **Gabriel:** Aceite, dê **Pull** e crie a branch `feat-censura`.
3. **Gabriel:** Crie uma string vazia `frase_oculta`. Percorra a frase original com `for`: se a letra for vogal, adicione `"*"` na string nova; se não, adicione a própria letra. Exiba o resultado final.

---

## Exercício 9: Caixa Eletrônico (Gabriel começa)
**Foco:** Algoritmos de subtração sucessiva com `while`.

**Passo a Passo:**
1. **Gabriel:** Branch `feat-saque-50`. Em `caixa.py`, peça um valor de saque. Use um `while` para subtrair 50 do valor enquanto ele for maior que 50, contando as cédulas. PR enviado.
2. **Lucas:** Aceite, dê **Pull** e crie a branch `feat-saque-completo`.
3. **Lucas:** Aplique a mesma lógica de loop para as notas de 20, 10 e 1 com o que sobrou do valor original. Isso ensina como construir algoritmos lógicos passo a passo.

---

## Exercício 10: O Hotfix (Lucas começa)
**Foco:** Gestão de crise e correção urgente em `main`.

**Passo a Passo:**
1. **O Erro:** Lucas, por pressa, altera o `caixa.py` na branch `main` diretamente, permitindo saques de valores negativos. Ele faz Commit e Push direto na `main`.
2. **A Detecção:** Gabriel dá **Pull**, roda o código e percebe que o sistema quebrou a lógica de segurança.
3. **A Correção:** Gabriel cria a branch `hotfix-seguranca`. Adiciona um `if valor <= 0: break`. Faz Commit, Push e marca o Lucas no PR como "URGENTE".
4. **Conclusão:** Lucas revisa e aceita imediatamente. Esse fluxo ensina que erros em produção exigem branches específicas de correção rápida (Hotfixes).

---
💡 **Dica Final:** No VS Code, use o atalho `Ctrl + Shift + G` para pular direto para a aba de Controle de Código-Fonte!
