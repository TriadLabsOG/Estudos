# 🚀 Roadmap: Python Profissional

## 🟢 FASE 1: O AMBIENTE PROFISSIONAL (Obrigatório)
- [ ] **Isolamento:** Aprender a criar e ativar `venv`.
- [ ] **Dependências:** Criar e usar o `requirements.txt`.
- [ ] **Segurança:** Usar `.env` e `python-dotenv` para chaves de API.
- [ ] **Tratamento de Erros:** Implementar blocos `try/except` com logs reais.

## 🟡 FASE 2: ENGENHARIA E DADOS (O Diferencial)
- [ ] **POO Básica:** Criar classes para organizar o código (ex: `class Curriculo`, `class Vaga`).
- [ ] **Gerador de PDF:** Usar `WeasyPrint` ou `ReportLab` para criar arquivos via código.
- [ ] **Banco de Dados (SQL):** Aprender `SELECT`, `INSERT` e `UPDATE` usando SQLite (nativo do Python).
- [ ] **Pydantic:** Validar dados que chegam de APIs ou Scrapers.

## 🟠 FASE 3: AUTOMAÇÃO AVANÇADA (O "Braço" do Robô)
- [ ] **Playwright:** Aprender a navegar, clicar e preencher formulários automaticamente.
- [ ] **Asyncio:** Rodar funções de forma assíncrona para ganhar velocidade.
- [ ] **Integração com IA:** Enviar prompts para o Gemini e tratar o retorno como JSON.

## 🔴 FASE 4: INFRAESTRUTURA E DEPLOY (Nível Vaga)
- [ ] **Docker:** Criar um `Dockerfile` para rodar seu enviador em qualquer PC.
- [ ] **Testes:** Criar testes simples com `pytest` para garantir que o PDF não saia em branco.
- [ ] **GitHub Actions:** Automatizar uma tarefa simples (CI/CD).

---

### 🛠️ Desafio Imediato para seu Projeto:
Para o seu enviador não "morrer" se um e-mail estiver errado, sua missão é:
1. Criar uma **Classe** de envio.
2. Colocar o envio dentro de um **Try/Except**.
3. Salvar o resultado num **Banco SQL** (para não enviar duas vezes para a mesma pessoa).
