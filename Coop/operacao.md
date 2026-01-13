# 🚀 Manual de Operação Assíncrona: Gabriel & Lucas (Python Edition)

Este documento estabelece o **Protocolo Padrão de Colaboração (SOP)**. O objetivo é garantir que o conhecimento seja retido, o código seja profissional (PEP-8) e a comunicação seja eficiente, simulando o fluxo de engenharia de empresas como **GitLab** e **Basecamp**.

---

## 1. Fundamentos da Metodologia Assíncrona

Trabalhar assincronamente não é "estudar sozinho", é **colaborar em tempos diferentes**.

* **Comunicação por Escrito:** A escrita é o modo padrão. O cérebro humano esquece; o repositório não. Se uma solução não está documentada na Issue ou no Código, ela não existe para a dupla.
* **Autonomia e Responsabilidade:** Você é dono do seu horário, mas é responsável pela sua entrega. A liberdade de estudar de madrugada exige a responsabilidade de deixar tudo pronto e explicado para o parceiro que estuda de manhã.
* **Public Over Private (Público sobre o Privado):** Nunca tire uma dúvida técnica no "privado" (WhatsApp). Se a dúvida for postada na **Issue**, ela se torna um ativo da dupla. Se o Lucas tiver a mesma dúvida do Gabriel amanhã, a solução já está escrita e organizada.

---

## 2. O Ciclo de Trabalho Detalhado

### Etapa 1: O Painel de Controle (A Issue)
A Issue funciona como o seu "Escritório Virtual". Uma **Sprint** é o nosso bloco de trabalho semanal. Vamos dividir o uso da Issue em duas partes: o **Descrição** (Contrato) e a **Comentários** (Execução).

**1. Como abrir:** Sempre que iniciarem um novo módulo (ex: Condicionais), criem uma Issue que servirá de guia.

**2. Descrição da Issue (O Planejamento):**
Cole o modelo abaixo na descrição inicial para definir as metas da semana.
```markdown
## 🏁 Sprint: [Nome do Módulo]
**Responsável:** @Gabriel / @Lucas

### 📝 Desafios (Metas da Semana)
- Aula 12
- Desafio 054 ao Desafio 063
```

**3. Comentários da Issue (O Diário de Execução):**
Durante a semana. Utilize os **comentários** da Issue para registrar o progresso real. Isso cria uma linha do tempo e notifica o parceiro.
* **Para Aprendizados:** Comente com a tag `[INSIGHT]`.
* **Para Erros:** Comente com a tag `[BUG]` ou `[DÚVIDA]`.

---

### Etapa 2: Desenvolvimento Local e Commits (O Código)
O trabalho de código deve ser limpo e isolado. Nunca mexa na branch `main` diretamente. 

1. **Branches Isoladas:** Cada bloco de exercícios deve ter sua branch própria. Isso permite que você trabalhe em algo novo sem estragar o código estável na Main.
2. **Organização de Pastas:** Respeite rigorosamente as pastas `/Gabriel` e `/Lucas`. Isso evita conflitos de arquivo (Merge Conflicts).
3. **Padrão de Commits Semânticos:** O commit é o registro do seu progresso. Use mensagens que expliquem o **quê** você fez:
    * `feat: resolve desafio 010 usando f-strings` (Novo exercício concluído).
    * `fix: corrige erro de lógica no calculo de juros` (Correção de bug).
    * `docs: atualiza manual de operação ou anotações` (Mudança apenas em texto).
    * `refactor: melhora legibilidade do código sem mudar lógica` (Limpeza).

### Etapa 3: Pull Requests e Code Review (A Auditoria)
O Pull Request (PR) é onde a revisão acontece. É a conversa sobre o código antes dele ser aceito.

**1. Como abrir o PR (Template de Descrição):**
Ao abrir o PR no GitHub, utilize o seguinte padrão no corpo do texto:
```markdown
## 📝 Descrição
Resolvi os desafios de manipulação de string. Foquei em aplicar os métodos `.strip()` e `.split()`.

## 🛠️ Checklist de Exercícios Realizados
- [ ] Desafio 022
- [ ] Desafio 023

## ⚖️ Auto-Revisão (Qualidade)
- [ ] Segui a PEP-8 (espaçamentos e nomes de variáveis).
- [ ] O código funciona e foi testado no terminal.
- [ ] Removi `prints` de teste e comentários desnecessários.
```

**2. O Papel do Reviewer (Como fazer o Code Review):**
O parceiro deve analisar o código e deixar comentários em linhas específicas:
```markdown
* **Crítica Construtiva:** "Nesta linha, você poderia usar `upper()` para garantir que a comparação não falhe com letras minúsculas."
* **Ajuste de PEP-8:** "Faltam 2 linhas em branco antes de definir esta função. #PEP8"
* **Aprovação:** Se estiver tudo perfeito, comente `LGTM` e clique no botão **Approve**.
```

### Etapa 4: Fechamento de Ciclo (O Áudio de Insights)
Após o Merge, envie o áudio no grupo da dupla para transmitir a experiência humana.

1. **Gatilho:** Assim que o parceiro aprovar seu código e você der o "Merge", vá ao grupo de mensagens.
2. **O Conteúdo (Roteiro 3-2-1):**
    * **(O Que):** "Finalizei a Issue #XX e o PR já foi mergeado."
    * **(A Dor):** "Apanhei muito da função `split()`, mas entendi que ela gera uma lista."
    * **(A Dica):** "Dica para o parceiro: Use o `enumerate()` no desafio 18, fica muito mais limpo."

---

## 3. Protocolo de Gestão de Conhecimento (Dúvidas)

### A. Como reportar uma Dúvida (Via Comentário)
Se travar e o parceiro estiver offline, poste um comentário na Issue seguindo este padrão:
1. **Contexto:** Em qual desafio/linha o problema ocorre.
2. **Expectativa:** "Eu queria que o código fizesse X, mas ele está retornando Y."
3. **O Erro:** Cole o erro do terminal (Traceback) entre crases (ex: `NameError`).
4. **O que já tentou:** "Já tentei mudar o tipo da variável e reiniciar o VS Code."

---

## 4. Padrões Técnicos e Qualidade (PEP-8)

O código deve seguir a **PEP-8** para que ambos leiam com fluidez:
* **Indentação:** Sempre 4 espaços (Configure seu VS Code para que a tecla TAB insira espaços).
* **Nomenclatura:** `nome_da_variavel_em_minusculo` (Snake Case).
* **Constantes:** Variáveis que não mudam em `CAIXA_ALTA`.
* **Comentários:** Use o `#` para explicar o **porquê** de uma lógica, não o que o comando faz.
    * *Bom:* `# Somando o total com a taxa de importação para o cálculo final`

---

## 5. Cronograma e Sprints

* **A Sprint:** Nosso ciclo semanal de domingo a sábado.
* **Planejamento:** No domingo, cria-se a Issue com o checklist de metas.
* **Execução:** Durante a semana, cada um faz no seu tempo, alimentando a Issue com comentários de dúvidas/bugs e abrindo PRs.
* **Fechamento:** A Sprint só é considerada "Finalizada" quando todas as Issues estão com status **Closed** e todos os Pull Requests foram aceitos na **Main**.

---

## 6. Gestão de Diferença de Ritmo (Cláusula de Sincronia)

Se um parceiro ficar "muito na frente" do outro (ex: um está no Mundo 2 e o outro no Mundo 1):

1. **O Líder não para, mas ensina:** Quem está na frente continua avançando, mas assume a responsabilidade de ser o **Mentor** nos Code Reviews de quem está atrás.
2. **Review Detalhado:** Quem está na frente deve deixar comentários mais didáticos nos PRs do parceiro, ajudando-o a acelerar com "atalhos" mentais.
3. **Pausa Estratégica:** Se a distância for maior que 1 Mundo inteiro, o parceiro avançado deve focar em **Refatorar** códigos antigos ou criar projetos extras (fora do Guanabara) até que a dupla se alinhe.

---

## 7. Glossário Operacional (Linguagem de Startup)

| Termo | Significado e Aplicação |
| :--- | :--- |
| **SOP** | Standard Operating Procedure. Se alguém errar o fluxo, diga: "Siga o SOP". |
| **LGTM** | Looks Good To Me. Use para aprovar o código do parceiro no Pull Request. |
| **Nitpick** | Sugestão estética que não impede o código de rodar. |
| **Refactor** | Reescrever o código para deixá-lo mais profissional/limpo. |

---
*Assinado: Gabriel & Lucas — Engenheiros de Software em construção.*
