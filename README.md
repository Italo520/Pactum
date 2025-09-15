# Pactum - Sistema de Gestão de Projetos e Contratos

Sistema web desenvolvido em Django para gestão completa de projetos e contratos, oferecendo controle financeiro, relatórios e painéis analíticos.

## 🚀 Características

- **Gestão de Projetos**: Controle completo do ciclo de vida de projetos
- **Gestão de Contratos**: Criação e acompanhamento de contratos com prestadores
- **Controle Financeiro**: Monitoramento de custos previstos vs. realizados
- **Relatórios**: Geração de relatórios em PDF e Excel
- **Dashboard Analytics**: Painéis com métricas e visualizações
- **Sistema de Usuários**: Autenticação com perfis e permissões diferenciadas
- **Integração de Pagamentos**: Suporte ao MercadoPago para processamento de pagamentos

## 🏗️ Arquitetura

### Backend
- **Framework**: Django 4.2.7
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Autenticação**: Sistema customizado com perfis de usuário
- **API**: Django REST Framework

### Frontend
- **UI Framework**: Bootstrap 5.3.0
- **Ícones**: Font Awesome 6.4.0
- **Charts**: Chart.js para visualização de dados
- **Forms**: Django Crispy Forms com Bootstrap 5

### Estrutura de Apps
```
apps/
├── core/           # Modelos base e utilitários
├── accounts/       # Autenticação e perfis de usuário
├── projetos/       # Gestão de projetos e ordens
├── contratos/      # Gestão de contratos e prestadores
├── clientes/       # Gestão de clientes
├── dashboard/      # Analytics e métricas
├── pagamentos/     # Integração com gateway de pagamento
└── relatorios/     # Geração de relatórios
```

## 🛠️ Tecnologias Utilizadas

### Backend
- Python 3.11+
- Django 4.2.7
- Django REST Framework
- PostgreSQL / SQLite
- Celery + Redis (tarefas assíncronas)
- Gunicorn (servidor WSGI)

### Relatórios e Documentos
- FPDF2 (geração de PDFs)
- OpenPyXL (geração de Excel)
- ReportLab (relatórios avançados)

### Integrações
- MercadoPago SDK (pagamentos)
- Django Extensions (ferramentas de desenvolvimento)

## 🚀 Configuração e Instalação

### Pré-requisitos
- Docker
- Docker Compose

### Instalação com Docker

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/pactum.git
cd pactum
```

2. **Configure as variáveis de ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
# Django Settings
SECRET_KEY=sua-chave-secreta-forte-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Settings
POSTGRES_DB=pactum_db
POSTGRES_USER=pactum_user
POSTGRES_PASSWORD=senha_forte_aqui
DATABASE_URL=postgresql://pactum_user:senha_forte_aqui@db:5432/pactum_db

# Payment Integration
MERCADOPAGO_ACCESS_TOKEN=seu-token-mercadopago
MERCADOPAGO_PUBLIC_KEY=sua-chave-publica-mercadopago

# Email Settings
DEFAULT_FROM_EMAIL=sistema@pactum.org.br
```

3. **Construa e execute os containers**
```bash
# Construir as imagens e subir os serviços
docker-compose up --build

# Ou execute em background
docker-compose up -d --build
```

4. **Execute as migrações**
```bash
docker-compose exec web python manage.py migrate
```

5. **Crie um superusuário**
```bash
docker-compose exec web python manage.py createsuperuser
```

6. **Acesse a aplicação**
A aplicação estará disponível em: http://localhost:8001

### Comandos Docker Úteis

```bash
# Parar os serviços
docker-compose down

# Ver logs dos serviços
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f web

# Executar comandos no container
docker-compose exec web python manage.py shell
docker-compose exec web python manage.py collectstatic --noinput

# Reconstruir apenas um serviço
docker-compose build web

# Reiniciar um serviço
docker-compose restart web

# Remover volumes e containers
docker-compose down -v --remove-orphans
```

### Instalação Local (sem Docker)

Se preferir instalar localmente sem Docker:

1. **Pré-requisitos**
- Python 3.10+
- PostgreSQL (opcional, pode usar SQLite)

2. **Clone e configure**
```bash
git clone https://github.com/seu-usuario/pactum.git
cd pactum
pip install -r requirements.txt
```

3. **Configure variáveis de ambiente**
```bash
export SECRET_KEY="sua-chave-secreta-aqui"
export DEBUG="True"
export ALLOWED_HOSTS="localhost,127.0.0.1"
export DATABASE_URL="sqlite:///./db.sqlite3"
```

4. **Execute migrações e inicie o servidor**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
```

### Deploy no Replit

O projeto está configurado para deploy automático no Replit com:
- Workflow configurado para desenvolvimento
- Configurações de deployment com Gunicorn
- Variáveis de ambiente configuradas

## 📊 Funcionalidades Principais

### Gestão de Projetos
- Criação e acompanhamento de projetos
- Sistema de requisições e ordens de serviço
- Controle de marcos e entregas
- Lançamentos financeiros

### Controle de Contratos
- Cadastro de prestadores (PF/PJ)
- Criação de contratos com itens detalhados
- Cálculo automático de impostos
- Geração de parcelas de pagamento

### Relatórios
- **Relatórios Financeiros**: Análise de custos e receitas
- **Relatórios de Projetos**: Status e progresso dos projetos
- **Relatórios de Contratos**: Acompanhamento de contratos
- **Exportação**: PDF e Excel para todos os relatórios

### Dashboard e Analytics
- Métricas financeiras em tempo real
- Gráficos de progresso de projetos
- Indicadores de performance de contratos
- Visualizações interativas com Chart.js

## 👥 Perfis de Usuário

- **Admin**: Acesso completo ao sistema
- **TI**: Gerenciamento técnico e usuários
- **Fiscal**: Acompanhamento e fiscalização
- **Financeiro**: Controle financeiro e pagamentos
- **Analista**: Análise de dados e relatórios
- **Cliente**: Acesso limitado a projetos específicos

## 🔧 Configuração de Produção

### Variáveis de Ambiente Obrigatórias
```env
SECRET_KEY=sua-chave-secreta-forte
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com
DATABASE_URL=postgresql://user:password@host:port/database
MERCADOPAGO_ACCESS_TOKEN=seu-token-mercadopago
MERCADOPAGO_PUBLIC_KEY=sua-chave-publica-mercadopago
```

### Configurações de Segurança
- CSRF protegido
- Cookies seguros configurados
- Middleware de auditoria implementado
- Logs de acesso e erro configurados

## 📋 Comandos Úteis

### Comandos Django com Docker
```bash
# Criar migrações
docker-compose exec web python manage.py makemigrations

# Aplicar migrações
docker-compose exec web python manage.py migrate

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic --noinput

# Executar testes
docker-compose exec web python manage.py test

# Shell do Django
docker-compose exec web python manage.py shell

# Importar dados legados
docker-compose exec web python manage.py import_legacy_data

# Backup do banco de dados
docker-compose exec db pg_dump -U pactum_user pactum_db > backup.sql

# Restaurar backup
docker-compose exec -T db psql -U pactum_user -d pactum_db < backup.sql
```

### Comandos Django Locais
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Executar testes
python manage.py test

# Shell do Django
python manage.py shell

# Importar dados legados
python manage.py import_legacy_data
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).

## 📞 Contato

Para dúvidas ou suporte, entre em contato:
- Email: contato@pactum.org.br
- Suporte Técnico: ti@pactum.org.br

---

Desenvolvido com ❤️ usando Django e Bootstrap