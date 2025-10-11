
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria um superusuário se nenhum existir com o nome de usuário "admin"'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.SUCCESS('Superusuário "admin" já existe.'))
        else:
            User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superusuário "admin" criado com sucesso.'))
