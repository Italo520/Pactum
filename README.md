# Pactum - Sistema de Gestão de Contratos

O Pactum é um sistema de gestão de projetos e contratos construído com Django. Ele oferece uma solução robusta para controlar custos, prazos, pagamentos e a relação com prestadores de serviço (Pessoa Física e Jurídica).

## 🚀 Visão Geral

Este projeto visa modernizar e estruturar a gestão de contratos, fornecendo uma plataforma centralizada com as seguintes funcionalidades:

-   **Gestão Completa**: Cadastro de clientes, prestadores, projetos e contratos.
-   **Controle Financeiro**: Gestão de parcelas, pagamentos e controle de inadimplência.
-   **Dashboard Analítico**: Visualização de KPIs e métricas importantes.
-   **Sistema de Alertas**: Notificações sobre prazos e status financeiros.
-   **Relatórios Personalizados**: Geração de relatórios em PDF e Excel.

## 📚 Documentação

Toda a documentação do projeto, incluindo guias de instalação, manuais de usuário e análises técnicas, está centralizada na pasta `docs/`.

-   [**Guia Completo (`docs/GUIA_COMPLETO.md`)**](./docs/GUIA_COMPLETO.md): Um guia unificado que cobre a instalação, o uso do sistema e detalhes técnicos.
-   [**Análise do Sistema Legado (`docs/analise_legado.md`)**](./docs/analise_legado.md): Análise técnica do sistema anterior que serviu de base para o Pactum.

## 🛠️ Tecnologias Utilizadas

-   **Back-end**: Django
-   **Front-end**: HTML/CSS/JavaScript (com build via `npm`/`pnpm`)
-   **Banco de Dados**: PostgreSQL
-   **Containerização**: Docker

---

## 🐳 Começando com Docker

A maneira mais simples e recomendada de executar o Pactum localmente é usando Docker e Docker Compose.

### Pré-requisitos
-   [Docker](https_//docs.docker.com/get-docker/)
-   [Docker Compose](https_//docs.docker.com/compose/install/)

### 1. Clonar o Repositório
```bash
git clone <repository-url>
cd pactum-system
```

### 2. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto, copiando o exemplo:
```bash
cp .env.example .env
```
O `.env` já vem com valores padrão para o ambiente de desenvolvimento. Se necessário, você pode personalizá-lo.

### 3. Subir os Containers
Com o Docker em execução, execute o seguinte comando na raiz do projeto:
```bash
docker-compose up --build
```
Este comando irá:
-   Construir a imagem do Django (se ainda não existir).
-   Iniciar os containers do `web` (aplicação Django) e `db` (banco de dados PostgreSQL).
-   Executar as migrações do banco de dados automaticamente.
-   Coletar os arquivos estáticos.

A aplicação estará disponível em [http_//localhost:5001](http_//localhost:5001).

### 4. Criar um Superusuário
Para acessar a área administrativa do Django, você precisará criar um superusuário. Em um novo terminal, com os containers em execução, execute:
```bash
docker-compose exec web python manage.py createsuperuser
```
Siga as instruções para criar seu usuário.

## ⚙️ Executando Comandos de Gerenciamento
Para executar comandos do `manage.py` (como `makemigrations`, `shell`, etc.), use `docker-compose exec`:
```bash
docker-compose exec web python manage.py <comando>
```

---

## 📦 Estrutura do `docker-compose.yml`
O `docker-compose.yml` define dois serviços principais:
-   `db`: O container do banco de dados PostgreSQL. Os dados são persistidos em um volume chamado `postgres_data`.
-   `web`: O container da aplicação Django, que depende do serviço `db`.

Para mais detalhes sobre a configuração, consulte a seção de **Deploy e Monitoramento** no [Guia Completo](./docs/GUIA_COMPLETO.md)
