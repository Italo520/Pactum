# 📚 Guia Completo do Sistema Pactum

## Sumário
1. [Visão Geral do Projeto](#-visão-geral-do-projeto)
2. [Arquitetura e Tecnologias](#-arquitetura-e-tecnologias)
3. [Manual de Instalação com Docker](#-manual-de-instalação-com-docker)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação via Docker Compose](#instalação-via-docker-compose)
    - [Entendendo o Ambiente Docker](#entendendo-o-ambiente-docker)
    - [Gerenciando a Aplicação com Docker Compose](#gerenciando-a-aplicação-com-docker-compose)
4. [Manual do Usuário](#-manual-do-usuário)
5. [Deploy e Monitoramento](#-deploy-e-monitoramento)
6. [Solução de Problemas](#-solução-de-problemas)
7. [Suporte Técnico](#-suporte-técnico)

---

## 🚀 Visão Geral do Projeto

O **Pactum** é uma plataforma completa para gestão de contratos de projetos de prestação de serviços. O sistema controla custos, prazos, pagamentos e oferece diferenciação completa entre prestadores Pessoa Física (PF) e Pessoa Jurídica (PJ).

### ✅ Funcionalidades Principais
- **Cadastro completo** de clientes, prestadores e projetos
- **Controle financeiro** com gestão de parcelas e pagamentos
- **Dashboard analítico** com indicadores visuais
- **Sistema de alertas** para prazos e inadimplência
- **Relatórios personalizados** para diferentes perfis de usuário
- **Diferenciação fiscal** automática entre PF e PJ

---

## 🛠️ Arquitetura e Tecnologias

- **Back-end**: Django
- **Front-end**: HTML, CSS, JavaScript (com build via `npm` ou `pnpm`)
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker

---

## 🔧 Manual de Instalação com Docker

A maneira recomendada para configurar e executar o ambiente de desenvolvimento do Pactum é utilizando Docker e Docker Compose. Isso garante um ambiente consistente e simplifica a configuração inicial.

### Pré-requisitos
-   [Docker](https_//docs.docker.com/get-docker/)
-   [Docker Compose](https_//docs.docker.com/compose/install/)

### Instalação via Docker Compose

#### 1. Clonar o Repositório
```bash
git clone <repository-url>
cd pactum-system
```

#### 2. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto, copiando o exemplo:
```bash
cp .env.example .env
```
O `.env` já vem com valores padrão para o ambiente de desenvolvimento. Se necessário, você pode personalizá-lo.

#### 3. Subir os Containers
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

#### 4. Criar um Superusuário
Para acessar a área administrativa do Django, você precisará criar um superusuário. Em um novo terminal, com os containers em execução, execute:
```bash
docker-compose exec web python manage.py createsuperuser
```
Siga as instruções para criar seu usuário.

### Entendendo o Ambiente Docker

#### `Dockerfile`
O `Dockerfile` é a receita para construir a imagem da nossa aplicação Django. Ele realiza os seguintes passos:
1.  **Usa uma imagem base do Python 3.10**: `FROM python:3.10-slim`.
2.  **Define variáveis de ambiente**: Para otimizações do Python.
3.  **Define o diretório de trabalho**: `WORKDIR /app`.
4.  **Instala dependências do sistema**: Como `libpq-dev` para a comunicação com o PostgreSQL.
5.  **Copia e instala as dependências Python**: `pip install -r requirements.txt`.
6.  **Copia o código da aplicação**: `COPY . /app/`.
7.  **Expõe a porta**: A porta `5000` é exposta para o Gunicorn.
8.  **Define o comando de inicialização**: `CMD ["gunicorn", ...]`.

#### `docker-compose.yml`
O `docker-compose.yml` orquestra a execução dos nossos containers. Ele define dois serviços:
-   `db`:
    -   **Imagem**: `postgres:15`.
    -   **Variáveis de Ambiente**: Configura o nome do banco, usuário e senha.
    -   **Volumes**: Garante que os dados do PostgreSQL sejam persistidos no volume `postgres_data`.
    -   **Healthcheck**: Verifica se o banco de dados está pronto para aceitar conexões.
-   `web`:
    -   **Build**: Constrói a imagem a partir do `Dockerfile` no diretório atual.
    -   **Comando**: Executa as migrações, coleta os arquivos estáticos e inicia o Gunicorn.
    -   **Volumes**: Mapeia o código local para dentro do container, permitindo o hot-reload.
    -   **Portas**: Mapeia a porta `5001` do host para a porta `5000` do container.
    -   **Variáveis de Ambiente**: Carrega as configurações do arquivo `.env`.
    -   **`depends_on`**: Garante que o container `web` só inicie após o `db` estar saudável.

### Gerenciando a Aplicação com Docker Compose

-   **Subir os containers em background**:
    ```bash
    docker-compose up -d
    ```
-   **Parar os containers**:
    ```bash
    docker-compose down
    ```
-   **Ver os logs**:
    ```bash
    docker-compose logs -f
    ```
-   **Executar um comando de gerenciamento**:
    ```bash
    docker-compose exec web python manage.py <comando>
    ```

---

## 📖 Manual do Usuário

... (O restante do manual do usuário permanece o mesmo) ...

---

## 🚀 Deploy e Monitoramento

### Deploy com Docker
O `docker-compose.yml` fornecido é otimizado para desenvolvimento. Para produção, considere as seguintes alterações:
-   **Remova o volume de código**: Em produção, o código deve ser copiado para a imagem durante o build, não montado a partir do host.
-   **Gerenciamento de Segredos**: Utilize um sistema de gerenciamento de segredos (como Docker Secrets ou variáveis de ambiente injetadas pelo provedor de nuvem) em vez do arquivo `.env`.
-   **Configurações de Produção**: Certifique-se de que `DEBUG=False` e `ALLOWED_HOSTS` esteja configurado corretamente.

### Monitoramento
-   **Logs**: Utilize o comando `docker-compose logs -f web` para acompanhar os logs da aplicação em tempo real.
-   **Health Check**: O health check do PostgreSQL no `docker-compose.yml` é um exemplo de como garantir a saúde dos serviços.

---

## 🔍 Solução de Problemas

### Erros ao subir os containers
-   **"Port is already allocated"**: Verifique se a porta `5001` ou `5434` não está em uso por outro serviço na sua máquina.
-   **"Service 'web' failed to build"**: Verifique os logs do build para identificar o erro. Pode ser um problema de rede ou uma dependência do sistema que falhou ao instalar.

### Problemas comuns no Django
-   **"Static files not found (404)"**: O comando no `docker-compose.yml` já executa `collectstatic`. Se encontrar problemas, verifique se o build do front-end (`npm run build`) foi executado antes de subir os containers.
-   **"Database doesn't exist"**: O `depends_on` e o `healthcheck` no `docker-compose.yml` devem prevenir isso, mas se ocorrer, verifique os logs do serviço `db`.

---

## 📞 Suporte Técnico

Para problemas ou dúvidas, abra uma issue no repositório do projeto no GitHub.
-   **GitHub**: https://github.com/Italo520