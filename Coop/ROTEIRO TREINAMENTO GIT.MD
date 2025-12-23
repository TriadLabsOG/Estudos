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

### 4. Resolução de Conflito (Simultâneo) ⚠️
* **Preparação:** Lucas cria `config.py` com `BANCO = "Original"` na `main`, faz commit e push. Ambos dão Pull.
* **Lucas:** Na branch `ajuste-lucas`, mude para `"PostgreSQL"`. Commit.
* **Gabriel:** Na branch `ajuste-gabriel`, mude a **mesma linha** para `"MySQL"`. Commit, Push e Merge no GitHub primeiro.
* **Resolução:** Lucas tentará dar Merge e o GitHub avisará o conflito. Lucas deve: `main` -> Pull -> volta para sua branch -> Clica em "Mesclar de... main" -> Escolhe uma opção no editor -> Stage (+) -> Commit.

### 5. Validador de Senha
* **Gabriel:** Crie a branch `feat-senha`. Em `seguranca.py`, verifique se `len(senha) > 8`. Commit e PR.
* **Lucas:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-seguranca-num`. Use um `for` e `.isdigit()` para avisar se a senha não tem números. Commit e PR.

### 6. Simulador de Financiamento
* **Lucas:** Crie a branch `feat-finan`. Em `finan.py`, peça Valor Total e Meses. Calcule a parcela simples. Commit e PR.
* **Gabriel:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-tabela`. Use um `for` para mostrar o saldo devedor diminuindo mês a mês. Commit e PR.

### 7. Sorteio de Grupos
* **Gabriel:** Crie a branch `feat-sorteio`. Importe `random` e use `random.shuffle()` em uma lista de nomes. Commit e PR.
* **Lucas:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-duplas`. Use um `for` com `range(0, len(lista), 2)` para imprimir os nomes em duplas. Commit e PR.

### 8. Contador e Censura
* **Lucas:** Crie a branch `feat-contar`. Em `texto.py`, conte quantos espaços existem em uma frase usando `for`. Commit e PR.
* **Gabriel:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-censura`. Percorra a frase e troque vogais por `*`. Commit e PR.

### 9. Caixa Eletrônico (Lógica Successiva)
* **Gabriel:** Crie a branch `feat-saque`. Em `caixa.py`, use `while` para contar quantas notas de 50 saem de um valor. Commit e PR.
* **Lucas:** Aceite o PR. Na `main` (após Pull), crie a branch `feat-notas-menores`. Use a sobra do valor anterior para contar notas de 10 e 1 real. Commit e PR.

### 10. O Hotfix (Urgência)
* **Lucas:** Na `main` (direto!), altere o `caixa.py` permitindo saques negativos (erro proposital). Commit e Push direto na `main`.
* **Gabriel:** Percebe o bug. Cria a branch `hotfix-seguranca`. Adiciona um `if valor < 0: return`. Commit, Push e PR marcado como "Urgente".
* **Fim:** Lucas aceita o PR e ambos aprendem a nunca mexer na `main` sem testar antes!
