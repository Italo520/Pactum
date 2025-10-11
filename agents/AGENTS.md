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

## Backlog da Tarefas:


### **Tarefas Prioritárias (A Fazer)**

* **ID**: `FE-MIG-004`
    * **Título**: Correção Visual da Página de Login
    * **Descrição**: Ajustar o layout e os estilos da página de login (`login.html`) para corrigir as distorções visuais. Isso inclui redimensionar o logo, estilizar os campos de formulário e o botão de login com classes do Tailwind CSS, e garantir que o alinhamento geral da página esteja consistente com o novo design system.
    * **Agentes Envolvidos**: `Frontend-Agent`.

* **ID**: `BE-DEVOPS-001`
    * **Título**: Criação Automática de Superusuário
    * **Descrição**: Desenvolver um script ou comando de gerenciamento do Django para criar um superusuário (usuário: `admin`, email: `admin@admin.com`, senha: `admin`) se ele ainda não existir. Integrar este script ao `docker-compose.yml` para que seja executado na inicialização do container, logo após as migrações.
    * **Agentes Envolvidos**: `Backend_Developer_Agent`, `DevOps_Agent`.


### Tarefas em Andamento


### Tarefas Concluídas

