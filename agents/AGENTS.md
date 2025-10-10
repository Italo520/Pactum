# Painel de Controle e Tarefas dos Agentes de IA

Este documento centraliza o backlog de desenvolvimento do projeto Pactum e descreve o fluxo de trabalho para a equipe de agentes de IA. O **PM-Agent** é o principal responsável por manter este arquivo atualizado.

---

## Fluxo de Trabalho (Workflow)

Todas as tarefas devem seguir o ciclo de vida abaixo para garantir qualidade, consistência e documentação adequada.

1.  **Criação da Tarefa**: O **PM-Agent** cria uma nova tarefa na seção "Backlog" com uma descrição clara, critérios de aceitação e um ID único (ex: `TASK-001`).
2.  **Atribuição**: O **PM-Agent** move a tarefa para "Em Andamento" e a atribui ao(s) agente(s) principal(is) (`Backend-Agent`, `Frontend-Agent`).
3.  **Desenvolvimento**: O agente de desenvolvimento executa a tarefa.
    * Escreve o código da funcionalidade.
    * Cria/atualiza os testes unitários relevantes.
4.  **Revisão e Testes**: Após o desenvolvimento, a tarefa é passada para o **QA-Agent**.
    * O **QA-Agent** executa a suíte de testes completa (unitários, integração, etc.).
    * Se um bug for encontrado, a tarefa retorna ao desenvolvedor com um relatório detalhado.
    * Se os testes passarem, a tarefa é aprovada.
5.  **Implantação (Deploy)**: A tarefa é passada para o **DevOps-Agent**.
    * O **DevOps-Agent** integra o novo código à branch principal e realiza o deploy no ambiente de produção/homologação.
6.  **Documentação**: Em paralelo, a tarefa é sinalizada para o **Documentation-Agent**.
    * O **Docs-Agent** atualiza os manuais (`MANUAL_DO_USUARIO.md`, `MANUAL_DE_INSTALACAO.md`, etc.) conforme a nova funcionalidade.
7.  **Conclusão**: Após o deploy bem-sucedido e a atualização da documentação, o **PM-Agent** move a tarefa para "Concluído" e arquiva os detalhes.

---

## Backlog de Tarefas (exemplo)

### Tarefas Prioritárias (A Fazer)

* **ID**: `TASK-001`
    * **Título**: Implementar Autenticação de Dois Fatores (2FA)
    * **Descrição**: Adicionar uma camada extra de segurança no login. O usuário, após inserir a senha, deverá fornecer um código gerado por um aplicativo autenticador (como Google Authenticator).
    * **Critérios de Aceitação**:
        * Um usuário pode habilitar/desabilitar o 2FA em seu perfil.
        * O processo de login exige o código 2FA se estiver habilitado.
        * Códigos de recuperação devem ser gerados para o usuário.
    * **Agentes Envolvidos**: `Backend-Agent`, `Frontend-Agent`, `QA-Agent`, `Docs-Agent`.

* **ID**: `TASK-002`
    * **Título**: Módulo de Anexos em Projetos
    * **Descrição**: Permitir que os usuários façam upload de arquivos (documentos, planilhas, imagens) e os associem a um projeto específico.
    * **Critérios de Aceitação**:
        * Na página de detalhes de um projeto, deve haver uma seção para anexos.
        * Usuários podem fazer upload de novos arquivos.
        * Usuários podem baixar ou excluir arquivos existentes.
    * **Agentes Envolvidos**: `Backend-Agent`, `Frontend-Agent`, `QA-Agent`, `Docs-Agent`.

### Tarefas em Andamento

* **ID**: `TASK-003`
    * **Título**: [BUG] Valor Total em Contratos não considera Itens Adicionais
    * **Descrição**: O campo "Valor Total" na lista de contratos está exibindo apenas o valor base do contrato, sem somar os valores dos "Itens de Contrato" associados a ele.
    * **Critérios de Aceitação**:
        * O valor total do contrato deve ser a soma do valor base + todos os itens.
        * O cálculo deve ser refeito sempre que um item for adicionado, editado ou removido.
    * **Agentes Envolvidos**: `Backend-Agent`, `QA-Agent`.

### Tarefas Concluídas

* **ID**: `TASK-004`
    * **Título**: Otimizar Query do Dashboard Principal
    * **Descrição**: A query que calcula os totais de "previsto vs. realizado" no dashboard principal está lenta. É preciso otimizá-la usando `select_related` ou `prefetch_related` do Django para reduzir o número de consultas ao banco de dados.
    * **Critérios de Aceitação**:
        * O tempo de carregamento do dashboard deve ser reduzido em pelo menos 30%.
        * Os dados exibidos devem permanecer corretos.
    * **Agentes Envolvidos**: `Backend-Agent`, `QA-Agent`.
