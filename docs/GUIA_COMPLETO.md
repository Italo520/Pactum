# 📚 Guia Completo do Sistema Pactum

## Sumário
1. [Visão Geral do Projeto](#-visão-geral-do-projeto)
2. [Arquitetura e Tecnologias](#-arquitetura-e-tecnologias)
3. [Manual de Instalação](#-manual-de-instalação)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação Local](#instalação-local)
    - [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
    - [Configuração de Produção](#configuração-de-produção)
4. [Manual do Usuário](#-manual-do-usuário)
    - [Acesso ao Sistema](#acesso-ao-sistema)
    - [Dashboard Principal](#dashboard-principal)
    - [Gestão de Clientes](#gestão-de-clientes)
    - [Gestão de Prestadores](#gestão-de-prestadores)
    - [Gestão de Projetos](#gestão-de-projetos)
    - [Gestão de Contratos](#gestão-de-contratos)
    - [Controle Financeiro](#controle-financeiro)
    - [Relatórios](#relatórios)
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

## 🔧 Manual de Instalação

### Pré-requisitos

#### Requisitos de Sistema
- **Python**: 3.10 ou superior
- **Node.js**: v18 ou superior (para build do front-end)
- **npm** ou **pnpm**
- **Banco de Dados**: PostgreSQL
- **Memória RAM**: Mínimo 2GB (recomendado 4GB)
- **Espaço em Disco**: Mínimo 1GB livre

#### Dependências Principais (Back-end)
```python
Django==4.2.7
django-crispy-forms==2.1
crispy-bootstrap5==0.7
... # (demais dependências do requirements.txt)
```

### Instalação Local

#### 1. Clonar o Repositório
```bash
git clone <repository-url>
cd pactum-system
```

#### 2. Configurar Ambiente Virtual (Python)
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3. Instalar Dependências (Back-end)
```bash
pip install -r requirements.txt
```

#### 4. Instalar Dependências e Build (Front-end)
O front-end utiliza `npm` ou `pnpm` para gerenciar as dependências de CSS e JavaScript.

```bash
# Usando npm
npm install
npm run build

# Ou usando pnpm
pnpm install
pnpm run build
```

#### 5. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:pass@host:port/db
```

#### 6. Executar Migrações do Banco
```bash
python manage.py migrate
```

#### 7. Criar Superusuário
```bash
python manage.py createsuperuser
```

#### 8. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

### Configuração do Banco de Dados

O sistema utiliza a variável de ambiente `DATABASE_URL` para configurar a conexão com o PostgreSQL.

```env
# Exemplo de .env
DATABASE_URL=postgresql://pactum_user:sua_senha@localhost:5432/pactum_db
```

### Configuração de Produção

#### 1. Configurações de Segurança (`settings.py`)
```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
SECURE_SSL_REDIRECT = True
```

#### 2. Coletar Arquivos Estáticos
```bash
python manage.py collectstatic --noinput
```

#### 3. Servidor de Aplicação (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:8000 pactum.wsgi:application
```

---

## 📖 Manual do Usuário

### Acesso ao Sistema

1.  Acesse a URL do sistema.
2.  Digite seu **usuário** e **senha**.
3.  Clique em "Entrar".

### Dashboard Principal

O Dashboard é a tela inicial com uma visão geral do sistema, incluindo KPIs, gráficos sobre projetos e status financeiro.

### Gestão de Clientes

- Para **cadastrar**, acesse "Clientes" > "Novo Cliente" e preencha os dados (PF/PJ).
- Para **consultar** ou **editar**, utilize a lista de clientes.

### Gestão de Prestadores

- Para **cadastrar**, acesse "Contratos" > "Prestadores" > "Novo Prestador".
- O sistema diferencia **Pessoa Física (PF)** e **Pessoa Jurídica (PJ)**, aplicando regras fiscais automáticas.

### Gestão de Projetos

- Para **criar**, acesse "Projetos" > "Novo Projeto".
- Monitore o **status** (ex: "Em Andamento", "Concluído") e o **controle de custos** (Previsto vs. Realizado).

### Gestão de Contratos

- Para **criar**, acesse "Contratos" > "Novo Contrato".
- Defina a **modalidade de pagamento** (único, parcelado).
- Acompanhe o **status do contrato** (ex: "Lançado", "Assinado").

### Controle Financeiro

- As **parcelas** são geradas automaticamente a partir dos contratos.
- Para **registrar um pagamento**, acesse os detalhes do contrato, encontre a parcela e clique em "Registrar Pagamento".
- O sistema possui controle de **inadimplência** com alertas e relatórios.

### Relatórios

O sistema oferece relatórios financeiros, de projetos e de contratos. Para gerar:
1.  Acesse "Relatórios".
2.  Selecione o tipo e defina os filtros.
3.  Exporte em PDF ou Excel.

---

## 🚀 Deploy e Monitoramento

### Deploy com Docker
O projeto inclui um `Dockerfile` e `docker-compose.yml` para facilitar o deploy.
```bash
# Build da imagem
docker build -t pactum-system .

# Executar com Docker Compose
docker-compose up -d
```

### Monitoramento
- **Logs**: Verifique os logs da aplicação para monitorar erros e acessos.
- **Health Check**: A página de admin (`/admin/`) pode ser usada para um health check básico.

---

## 🔍 Solução de Problemas

### "ModuleNotFoundError"
- **Solução**: Certifique-se de que o ambiente virtual está ativado e execute `pip install -r requirements.txt`.

### "Database doesn't exist"
- **Solução**: Verifique sua `DATABASE_URL` e execute `python manage.py migrate`.

### "Static files not found (404)"
- **Solução (Desenvolvimento)**: Verifique se o build de front-end (`npm run build`) foi executado.
- **Solução (Produção)**: Execute `python manage.py collectstatic --noinput`.

---

## 📞 Suporte Técnico

Para problemas ou dúvidas, abra uma issue no repositório do projeto no GitHub.
- **GitHub**: https://github.com/Italo520