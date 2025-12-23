# Guia Mestre do Git (Focado no Fluxo do VS Code)

Este guia unifica os conceitos teóricos profundos com a prática profissional, explicando como cada etapa funciona "por baixo do capô" e como você a vê no VS Code.

---

## 1. Repository (Repositório ou "Repo")
É o **banco de dados de versões** do seu projeto. Diferente de uma pasta comum, ele possui uma "memória perfeita" de tudo o que já aconteceu.

* **A Pasta Oculta (.git):** Tudo é vigiado por uma pasta oculta `.git`. Se você deletar isso, o histórico some.
* **Os 3 Estados (Essencial para o VS Code):**
    O Git não salva tudo de uma vez. Ele organiza o salvamento em etapas, visíveis na aba "Source Control" (ícone de ramificação) do VS Code:
    1.  **Working Directory (Changes):** São os arquivos que você acabou de editar. No VS Code, eles aparecem na lista "Changes" (Alterações). O Git sabe que mudaram, mas ainda não estão prontos para serem salvos.
    2.  **Staging Area (Staged Changes):** É a "Área de Preparação". Quando você clica no **`+`** ao lado de um arquivo no VS Code, ele sobe para a lista "Staged Changes". Isso significa: *"Vou incluir este arquivo no próximo commit"*.
    3.  **Repository (Commitado):** Quando a foto é tirada e salva permanentemente no histórico.
* **Local vs Remoto:** O **Local** é o seu PC. O **Remoto** é o GitHub/GitLab.

## 2. Branch (Ramificação)
Imagine o projeto como uma árvore. A `main` é o tronco. Uma `branch` é um galho que você cria para testar algo novo sem serrar o tronco por engano.

* **Ponteiro Móvel:** Tecnicamente, a branch é só uma etiqueta apontando para um commit. É muito leve.
* **No VS Code:** O nome da sua branch atual aparece no **canto inferior esquerdo** da janela (ex: `main` ou `feature/login`). Clicar ali permite criar ou trocar de branch.
* **Isolamento:** Se você quebrar o código na branch `teste`, a branch `main` continua funcionando perfeitamente.

## 3. Commit (O "Salvar" Profissional)
O commit é um ponto na história (um checkpoint). Ele tira uma "foto" (snapshot) exata de como os arquivos estavam naquele momento.

* **Atomicidade (A Regra de Ouro):**
    * **Conceito:** Um commit deve fazer **uma única coisa**.
    * **Exemplo:** Não misture "Arrumar cor do botão" com "Refazer o banco de dados" no mesmo commit.
    * **Por que separar?** Se o banco de dados der erro e você precisar desfazer (reverter), você não perde o ajuste da cor do botão.
    * **No VS Code:** É por isso que você não deve clicar no botão "Commit" geral sem pensar. Você deve ir na lista de arquivos, clicar no `+` apenas nos arquivos relacionados àquela tarefa específica, commitar, e depois repetir o processo para a próxima tarefa.
* **Metadados:** Todo commit tem um ID único (Hash), autor, data e uma mensagem obrigatória.

## 4. Push (Empurrar para a Nuvem)
Você fez commits no seu computador (Local). O `Push` envia essas "fotos" para o servidor (GitHub).

* **Sincronização:** É o ato de upload.
* **Bloqueio de Segurança:** O Git não deixa você dar Push se houver novidades no servidor que você ainda não baixou. Ele diz: *"Ei, seu colega subiu código novo. Baixe (Pull) primeiro, misture com o seu, garanta que funciona, e depois suba (Push)"*.
* **No VS Code:** Geralmente é o botão azul "Sync Changes" ou a opção "Push" no menu de três pontos `...`.

## 5. Fetch (A Espiada Segura)
O `Fetch` vai até o servidor e pergunta: "Tem novidade?". Ele baixa as atualizações para o seu PC, mas as deixa escondidas, **sem mexer no seu código de trabalho**.

* **Para que serve:** É uma forma cautelosa de ver o que o time está fazendo.
* **No VS Code:** O VS Code costuma fazer isso automaticamente em segundo plano (o ícone de sincronizar fica girando) para te avisar "Ei, tem 3 commits para baixar".

## 6. Pull (Puxar e Misturar)
O `Pull` é a combinação de dois passos:
1.  **Fetch:** Baixa as novidades.
2.  **Merge:** Tenta encaixar as novidades no seu arquivo aberto agora.

* **O Perigo (Conflitos):** Se você editou a linha 10 e seu colega também editou a linha 10, o Git entra em pânico. Ele para tudo e diz: "Conflito!".
* **No VS Code:** Quando dá conflito, o VS Code pinta o código de cores diferentes e mostra botões como "Accept Current Change" (Ficar com o meu) ou "Accept Incoming Change" (Aceitar o que veio da internet).

## 7. Pull Request (PR)
Isso acontece **fora** do VS Code (geralmente no site do GitHub), embora existam extensões para fazer dentro dele.

* **O Pedido:** Você diz ao dono do projeto: *"Terminei minha branch. Revise meu código e, se estiver bom, puxe (Pull) para a Main"*.
* **Code Review:** É a etapa de qualidade. Onde o time discute se o código está seguro e bem escrito antes de virar oficial.

## 8. Merge (A Fusão)
É o momento em que duas linhas do tempo se juntam.

* **Sucesso:** Se não houver conflitos, os códigos se misturam automaticamente.
* **Histórico:** O Merge cria um "nó" na árvore do histórico, simbolizando que o trabalho paralelo foi concluído e integrado.

---

### Exemplo Prático: O Jeito "VS Code" de fazer Atomic Commits

**Cenário:** Você alterou dois arquivos: `Login.js` (correção de bug) e `Estilo.css` (mudança de cor do site).

**❌ O Jeito Errado (Preguiçoso):**
Escrever "Arrumei tudo" na caixa de mensagem e clicar em *Commit* (enviando os dois arquivos juntos).
*Problema:* Se a cor ficar feia e reverterem o commit, o bug do login volta a existir.

**✅ O Jeito Certo (Atômico no VS Code):**

1.  Vá na aba **Source Control** (o ícone de grafo).
2.  Passe o mouse sobre `Login.js` e clique no **`+`**.
    * *O arquivo vai para a lista "Staged Changes". O `Estilo.css` continua embaixo.*
3.  Escreva na mensagem: "Fix: corrige erro de senha no login".
4.  Clique no **Check (✔)** ou "Commit".
5.  Agora, clique no **`+`** do `Estilo.css`.
6.  Escreva na mensagem: "Style: altera cor de fundo para azul".
7.  Clique no **Check (✔)** novamente.

**Resultado:** Você fez dois "Saves" perfeitos e organizados, prontos para enviar (Push).
