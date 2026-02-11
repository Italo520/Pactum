# populate_data.py
"""
Script para popular o banco de dados com dados de exemplo
para melhor visualização das telas do sistema Pactum
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from faker import Faker
import random

from apps.clientes.models import Cliente
from apps.contratos.models.prestador import Prestador
from apps.contratos.models.contrato import Contrato
from apps.projetos.models.projeto import Projeto

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Popula banco de dados com dados de exemplo'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Limpa dados existentes antes de popular',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Limpando dados existentes...'))
            Cliente.objects.all().delete()
            Prestador.objects.all().delete()
            Contrato.objects.all().delete()
            Projeto.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✓ Dados limpos'))

        self.stdout.write(self.style.MIGRATE_HEADING('\n🚀 Iniciando população de dados...'))

        # Criar clientes
        self.stdout.write('Criando clientes...')
        clientes = self.create_clientes(15)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(clientes)} clientes criados'))

        # Criar prestadores
        self.stdout.write('Criando prestadores...')
        prestadores = self.create_prestadores(10)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(prestadores)} prestadores criados'))

        # Criar projetos
        self.stdout.write('Criando projetos...')
        projetos = self.create_projetos(20)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(projetos)} projetos criados'))

        # Criar contratos
        self.stdout.write('Criando contratos...')
        contratos = self.create_contratos(25, prestadores)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(contratos)} contratos criados'))

        self.stdout.write(self.style.SUCCESS('\n✅ População de dados concluída com sucesso!'))

    def create_clientes(self, count):
        clientes = []
        for i in range(count):
            tipo = random.choice(['F', 'J'])
            
            if tipo == 'F':
                cliente = Cliente(
                    tipo_pessoa='F',
                    nome=fake.name(),
                    cpf=fake.cpf(),
                    email=fake.unique.email(),
                    telefone=fake.phone_number()
                )
            else:
                empresa = fake.company()
                cliente = Cliente(
                    tipo_pessoa='J',
                    nome=empresa,
                    razao_social=empresa + ' LTDA',
                    cnpj=fake.cnpj(),
                    email=fake.unique.company_email(),
                    telefone=fake.phone_number()
                )
            
            cliente.save()
            clientes.append(cliente)
        
        return clientes

    def create_prestadores(self, count):
        prestadores = []
        
        for i in range(count):
            tipo = random.choice(['PF', 'PJ'])
            
            if tipo == 'PF':
                prestador = Prestador(
                    tipo_pessoa='PF',
                    nome=fake.name(),
                    cpf=fake.cpf(),
                    rg=fake.rg(),
                    email=fake.unique.email(),
                    telefone=fake.phone_number(),
                    cep=fake.postcode(),
                    logradouro=fake.street_name(),
                    numero=str(fake.building_number()),
                    bairro=fake.neighborhood(),
                    cidade=fake.city(),
                    uf=fake.state_abbr(),
                    banco='Banco do Brasil',
                    agencia=f'{random.randint(1000, 9999)}',
                    conta=f'{random.randint(10000, 99999)}-{random.randint(0, 9)}',
                    tipo_conta='corrente',
                    ativo=True
                )
            else:
                empresa = fake.company()
                prestador = Prestador(
                    tipo_pessoa='PJ',
                    nome=empresa + ' LTDA',
                    nome_fantasia=empresa,
                    cnpj=fake.cnpj(),
                    inscricao_estadual=f'{random.randint(100000000, 999999999)}',
                    email=fake.unique.company_email(),
                    telefone=fake.phone_number(),
                    cep=fake.postcode(),
                    logradouro=fake.street_name(),
                    numero=str(fake.building_number()),
                    bairro=fake.neighborhood(),
                    cidade=fake.city(),
                    uf=fake.state_abbr(),
                    banco='Caixa Econômica',
                    agencia=f'{random.randint(1000, 9999)}',
                    conta=f'{random.randint(10000, 99999)}-{random.randint(0, 9)}',
                    tipo_conta='corrente',
                    ativo=True
                )
            
            prestador.save()
            prestadores.append(prestador)
        
        return prestadores

    def create_projetos(self, count):
        projetos = []
        hoje = timezone.now().date()
        
        situacoes = ['1', '2', '3', '4', '5', '6']
        pesos_situacao = [0.1, 0.4, 0.1, 0.05, 0.05, 0.3]  # Mais projetos em andamento
        
        for i in range(1, count + 1):
            situacao = random.choices(situacoes, weights=pesos_situacao)[0]
            
            # Datas baseadas na situação
            if situacao == '1':  # Aguardando início
                data_inicio = hoje + timedelta(days=random.randint(5, 60))
                data_encerramento = data_inicio + timedelta(days=random.randint(90, 365))
            elif situacao == '6':  # Concluído
                data_encerramento = hoje - timedelta(days=random.randint(1, 180))
                data_inicio = data_encerramento - timedelta(days=random.randint(90, 365))
            else:  # Em andamento, paralisado, suspenso, cancelado
                data_inicio = hoje - timedelta(days=random.randint(30, 180))
                data_encerramento = hoje + timedelta(days=random.randint(30, 180))
            
            projeto = Projeto(
                cod_projeto=i,
                nome=f"Projeto {fake.catch_phrase()}",
                data_inicio=data_inicio,
                data_encerramento=data_encerramento,
                valor=Decimal(str(random.randint(10000, 500000))),
                situacao=situacao
            )
            
            projeto.save()
            projetos.append(projeto)
        
        return projetos

    def create_contratos(self, count, prestadores):
        contratos = []
        hoje = timezone.now().date()
        
        situacoes = ['1', '2', '3', '4', '5', '6']
        pesos_situacao = [0.1, 0.5, 0.05, 0.05, 0.1, 0.2]
        
        for i in range(1, count + 1):
            prestador = random.choice(prestadores)
            situacao = random.choices(situacoes, weights=pesos_situacao)[0]
            
            # Datas
            if situacao == '6':  # Concluído
                data_fim = hoje - timedelta(days=random.randint(1, 90))
                data_inicio = data_fim - timedelta(days=random.randint(180, 365))
            else:
                data_inicio = hoje - timedelta(days=random.randint(30, 90))
                data_fim = hoje + timedelta(days=random.randint(60, 365))
            
            valor = Decimal(str(random.randint(5000, 200000)))
            parcelas = random.choice([1, 3, 6, 12, 24])
            
            contrato = Contrato(
                num_contrato=f'{i:04d}/{hoje.year}',
                cod_ordem=random.randint(1000, 9999),
                descricao=fake.sentence(nb_words=8),
                cpf_cnpj=prestador.get_documento_principal(),
                contratado=prestador.nome,
                tipo_pessoa=1 if prestador.tipo_pessoa == 'PF' else 2,
                data_inicio=data_inicio,
                data_fim=data_fim,
                valor=valor,
                parcelas=parcelas,
                data_parcela_inicial=data_inicio + timedelta(days=30),
                situacao=situacao
            )
            
            contrato.save()
            contratos.append(contrato)
        
        return contratos
