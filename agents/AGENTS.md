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

## Backlog da Tarefas: Migração Completa do Front-end

**Épico:** Refatorar a interface do usuário do sistema Pactum, substituindo o framework Bootstrap por uma stack moderna composta por Tailwind CSS, shadcn/ui e Aceternity UI.
**Objetivo:** Modernizar a UI/UX, melhorar a responsividade e criar um sistema de design coeso e de fácil manutenção.

### Tarefas Prioritárias (A Fazer)

* **ID**: `FE-MIG-002`
    * **Título**: Refatoração do Layout Estrutural (Base, Sidebar e Navbar)
    * **Descrição**: Reconstruir os componentes centrais da interface que são compartilhados por todas as páginas: o template base, a barra de navegação lateral (sidebar) e o cabeçalho (navbar), utilizando classes do Tailwind CSS e componentes `shadcn/ui` se aplicável.
    * **Critérios de Aceitação**:
        * O arquivo `base/base.html` define uma estrutura de layout flexível e responsiva com áreas para sidebar, header e conteúdo principal.
        * Os arquivos `base/sidebar.html` e `base/navbar.html` são recriados sem nenhuma classe Bootstrap e com uma navegação funcional.
        * O novo layout não apresenta quebras visuais em resoluções de desktop, tablet e mobile.
    * **Agentes Envolvidos**: `Frontend-Agent`, `UI-UX-Agent`.

* **ID**: `FE-MIG-003`
    * **Título**: Refatoração das Telas de Autenticação e Perfil
    * **Descrição**: Migrar o design das telas de login, visualização e edição de perfil de usuário para a nova stack, focando em formulários limpos e usabilidade.
    * **Critérios de Aceitação**:
        * A página de login (`accounts/login.html`) utiliza os componentes `Card`, `Input`, `Label` e `Button` do `shadcn/ui`.
        * As páginas de perfil (`accounts/profile.html` e `accounts/profile_edit.html`) são redesenhadas com um layout limpo, utilizando a nova estrutura de componentes.
        * Toda a funcionalidade de login e edição de perfil permanece intacta.
    * **Agentes Envolvidos**: `Frontend-Agent`, `QA-Agent`.

* **ID**: `FE-MIG-004`
    * **Título**: Refatoração do Módulo de Clientes (CRUD)
    * **Descrição**: Atualizar a interface de todas as operações (Criar, Ler, Atualizar, Deletar) do módulo de Clientes, substituindo tabelas, formulários e botões antigos.
    * **Critérios de Aceitação**:
        * A lista de clientes (`clientes/cliente_list.html`) utiliza o componente `Table` do `shadcn/ui`.
        * Os formulários (`clientes/cliente_form.html`) são reconstruídos com os novos componentes de formulário.
        * A página de detalhes (`clientes/cliente_detail.html`) exibe as informações do cliente de forma clara, utilizando `Card`.
        * A tela de confirmação de exclusão (`clientes/cliente_confirm_delete.html`) é estilizada, preferencialmente como um `AlertDialog`.
    * **Agentes Envolvidos**: `Frontend-Agent`, `QA-Agent`.

* **ID**: `FE-MIG-005`
    * **Título**: Refatoração do Módulo de Projetos (CRUD Completo)
    * **Descrição**: Migrar a interface de um dos módulos mais complexos do sistema, o de Projetos, que inclui a gestão de projetos, marcos, ordens de serviço e lançamentos financeiros.
    * **Critérios de Aceitação**:
        * A tela de detalhes do projeto (`projetos/projeto_detail.html`) é redesenhada para funcionar como um painel central, exibindo informações relacionadas de forma organizada.
        * Todas as listagens (projetos, ordens, etc.) são convertidas para o componente `Table`.
        * Todos os formulários do módulo (`projeto_form.html`, `marco_form.html`, `ordem_form.html`, etc.) são modernizados.
    * **Agentes Envolvidos**: `Frontend-Agent`, `UI-UX-Agent`, `QA-Agent`.

* **ID**: `FE-MIG-006`
    * **Título**: Refatoração do Módulo de Contratos
    * **Descrição**: Atualizar a interface do módulo de Contratos, incluindo a gestão de prestadores, itens de contrato e visualização de parcelas.
    * **Critérios de Aceitação**:
        * A página de detalhes do contrato (`contratos/contrato_detail.html`) apresenta um layout claro, separando dados principais, itens e pagamentos.
        * O modal de pagamento (`contratos/partials/modal_pagamento.html`) é reconstruído com os componentes `Dialog` ou `Drawer` do `shadcn/ui`.
        * A funcionalidade de pagamento via Mercado Pago não é afetada.
    * **Agentes Envolvidos**: `Frontend-Agent`, `QA-Agent`.

* **ID**: `FE-MIG-007`
    * **Título**: Redesenho do Dashboard e Telas de Analytics
    * **Descrição**: Criar um novo dashboard visualmente atraente e informativo, utilizando componentes de `Card` para KPIs e, se aplicável, componentes da `Aceternity UI` para dar um toque visual único e moderno aos gráficos e métricas.
    * **Critérios de Aceitação**:
        * O dashboard principal (`dashboard/index.html`) exibe os principais indicadores em `Card`s bem desenhados.
        * As páginas de analytics (`dashboard/analytics/*`) são redesenhadas para facilitar a leitura dos dados.
        * Os gráficos (gerados via Chart.js) são integrados de forma harmoniosa ao novo design.
    * **Agentes Envolvidos**: `Frontend-Agent`, `UI-UX-Agent`.

* **ID**: `FE-MIG-008`
    * **Título**: Verificação Final e Limpeza de Ativos
    * **Descrição**: Após a migração de todas as telas, realizar uma varredura completa no projeto para garantir que nenhum resquício do Bootstrap permaneça no código-fonte ou nos arquivos estáticos.
    * **Critérios de Aceitação**:
        * Nenhum arquivo `.html` no projeto contém classes como `container`, `row`, `col-md-*`, `btn-*`, etc.
        * A pasta `staticfiles/rest_framework/` (que contém o Bootstrap para o DRF) é a única exceção permitida.
        * Os arquivos CSS/JS do Bootstrap são removidos da pasta `static/`.
    * **Agentes Envolvidos**: `QA-Agent`, `Frontend-Agent`.

### Tarefas em Andamento
*(Nenhuma tarefa em andamento no momento)*

### Tarefas Concluídas
* **ID**: `FE-MIG-001`
    * **Título**: Configuração do Ambiente e Remoção do Bootstrap
    * **Descrição**: Preparar a base do projeto para a nova stack de front-end. Isso envolve remover completamente as dependências do Bootstrap e instalar e configurar o Tailwind CSS para compilar os estilos a partir dos arquivos de template do Django.
    * **Critérios de Aceitação**:
        * Os links para os arquivos CSS e JS do Bootstrap foram removidos do template `base/base.html`.
        * As dependências de front-end (`tailwindcss`, `postcss`, `autoprefixer`) estão listadas em um arquivo `package.json`.
        * O arquivo `tailwind.config.js` está criado e configurado para escanear todos os arquivos `.html` dentro da pasta `templates/`.
        * Um script de `build` consegue gerar um arquivo `output.css` na pasta `static/` que é carregado com sucesso no `base.html`.
    * **Agentes Envolvidos**: `Frontend-Agent`, `DevOps-Agent`.
