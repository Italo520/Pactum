
import re
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.projetos.models import Projeto, Requisicao, Ordem

class Command(BaseCommand):
    help = 'Importa dados legados do arquivo inserts_postgres.sql usando o ORM do Django.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando importação de dados legados...'))

        try:
            with open('inserts_postgres.sql', 'r', encoding='utf-8') as f:
                sql_content = f.read()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Arquivo inserts_postgres.sql não encontrado.'))
            return

        with transaction.atomic():
            self.stdout.write('Limpando tabelas existentes...')
            Ordem.objects.all().delete()
            Requisicao.objects.all().delete()
            Projeto.objects.all().delete()

            # Processar Projetos
            self.stdout.write('Processando projetos...')
            projetos_pattern = re.compile(r"INSERT INTO projetos \(codProjeto, nome, dataInicio, dataEncerramento, valor, situacao\) VALUES \((\d+), '([^']*)', '([^']*)', '([^']*)', (\d+\.\d+), '(\d+)'\);")
            projetos_data = projetos_pattern.findall(sql_content)
            
            projetos_to_create = []
            for p in projetos_data:
                projetos_to_create.append(Projeto(
                    cod_projeto=int(p[0]),
                    nome=p[1],
                    data_inicio=p[2],
                    data_encerramento=p[3],
                    valor=p[4],
                    situacao=p[5]
                ))
            
            Projeto.objects.bulk_create(projetos_to_create)
            self.stdout.write(self.style.SUCCESS(f'{len(projetos_to_create)} projetos importados.'))

            # Processar Requisições
            self.stdout.write('Processando requisições...')
            requisicao_pattern = re.compile(r"INSERT INTO requisicao \(codRequisicao, codProjeto, descricao, dataSolicitacao, dataLimite, valor, situacao\) VALUES \((\d+), (\d+), '([^']*)', '([^']*)', '([^']*)', (\d+\.\d+), '(\d+)'\);")
            requisicoes_data = requisicao_pattern.findall(sql_content)

            requisicoes_to_create = []
            for r in requisicoes_data:
                requisicoes_to_create.append(Requisicao(
                    cod_requisicao=int(r[0]),
                    cod_projeto_id=int(r[1]),
                    descricao=r[2],
                    data_solicitacao=r[3],
                    data_limite=r[4],
                    valor=r[5],
                    situacao=r[6]
                ))

            Requisicao.objects.bulk_create(requisicoes_to_create)
            self.stdout.write(self.style.SUCCESS(f'{len(requisicoes_to_create)} requisições importadas.'))

            # Processar Ordens
            self.stdout.write('Processando ordens...')
            ordem_pattern = re.compile(r"INSERT INTO ordem \(codOrdem, codRequisicao, descricao, dataSolicitacao, dataLimite, valor, situacao\) VALUES \((\d+), (\d+), '([^']*)', '([^']*)', '([^']*)', (\d+\.\d+), '(\d+)'\);")
            ordens_data = ordem_pattern.findall(sql_content)

            ordens_to_create = []
            for o in ordens_data:
                ordens_to_create.append(Ordem(
                    cod_ordem=int(o[0]),
                    cod_requisicao_id=int(o[1]),
                    descricao=o[2],
                    data_solicitacao=o[3],
                    data_limite=o[4],
                    valor=o[5],
                    situacao=o[6]
                ))
            
            Ordem.objects.bulk_create(ordens_to_create)
            self.stdout.write(self.style.SUCCESS(f'{len(ordens_to_create)} ordens importadas.'))

        self.stdout.write(self.style.SUCCESS('Importação de dados legados concluída com sucesso!'))
