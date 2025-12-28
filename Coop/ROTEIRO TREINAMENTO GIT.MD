# 🎓 Masterclass Git & Python: Fluxo Lucas & Gabriel

Este roteiro foca no **GitHub Flow**. O objetivo é dominar o ciclo: 
`Nova Branch` -> `Código` -> `Commit` -> `Push` -> `Pull Request` -> `Merge`.

---

## 📖 Legenda e Guia de Sobrevivência (Estude isso!)

### 🛠️ Comandos Git no VS Code
| Função | O que faz / Como evitar erros |
| :--- | :--- |
| **Branch (Ramificação)** | Uma cópia do código para testes. **Dica:** NUNCA edite a `main` diretamente. |
| **Sincronizar (Pull)** | Baixa as atualizações do colega. **Sempre** dê Pull antes de criar uma branch nova. |
| **Stage (+)** | O botão de "+" ao lado do arquivo. Avisa ao Git: "quero salvar este arquivo". |
| **Commit (✔)** | Salva a foto do seu código localmente. Exige uma mensagem explicativa. |
| **Push (Nuvem)** | Envia seus commits para o GitHub. Sem isso, o colega não vê seu código. |
| **Pull Request (PR)** | Pedido no site do GitHub para unir sua branch à `main`. |
| **Merge** | Ação de aceitar o PR e "misturar" os códigos. |

### 🏷️ Padrões de Commit (Prefixos)
Use estes prefixos para manter o histórico organizado:
* `feat:` (Nova funcionalidade ou arquivo)
* `fix:` (Correção de um erro/bug)
* `chore:` (Mudanças pequenas, comentários ou organização)
* `docs:` (Apenas documentação/texto)

---

## ⚡ Exercícios Práticos (Foco no Git)

### 1. Média Acadêmica
* **Lucas:** Na `main`, crie a branch `feat-media`. Em `notas.py`, crie uma função que recebe uma lista e retorna a média. `Commit: feat: add calculo de media`. Push e abra PR.
* **Gabriel:** Aceite o PR. No VS Code, mude para `main`, dê **Pull**. Crie a branch `feat-validacao`. No arquivo, use um `if` para validar se a nota está entre 0 e 10. `Commit: fix: valida intervalo de notas`. Push e PR.

### 2. Estoque Simples
* **Gabriel:** Na `main` (após Pull), crie a branch `feat-estoque`. Em `estoque.py`, crie um dicionário `{produto: preco}` e um `for` que imprime produtos caros (> 50). Commit, Push e PR.
* **Lucas:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-busca`. Adicione uma função que recebe o nome de um produto e diz se ele está no estoque. Commit, Push e PR.

### 3. Tabuada com Histórico
* **Lucas:** Crie a branch `feat-tabuada`. Em `tabuada.py`, use um `for` para gerar a tabuada de um número e salve os resultados em uma lista com `.append()`. Commit, Push e PR.
* **Gabriel:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-loop`. Envolva o código em um `while True` para repetir o processo até o usuário mandar parar. Commit, Push e PR.