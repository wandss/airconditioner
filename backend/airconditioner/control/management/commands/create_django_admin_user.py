from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

import os

class Command(BaseCommand):
    """Creates a django super user case it doesn't exist"""

    help = "Creates a django super user case it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin username")
        parser.add_argument('--email', help="Admin email address")
        parser.add_argument('--password', help="Admins password")

    def getOptionsfromEnv(self):
        "Overrrides values passed from arguments by environment variables"

        env_vars = ['DJANGO_ADMIN_NAME', 'DJANGO_ADMIN_EMAIL',
                'DJANGO_ADMIN_PASSWORD']

        model_names = {'DJANGO_ADMIN_NAME': 'username',
                'DJANGO_ADMIN_EMAIL':'email',
                'DJANGO_ADMIN_PASSWORD':'password'}

        options = {}

        for var_name in env_vars:
            if var_name in os.environ:
                options[model_names[var_name]] = os.environ[var_name]

        return options

    def handle(self, *args, **options):
        User = get_user_model()
        env_options = self.getOptionsfromEnv()

        if env_options.items():
            options = env_options

        if not User.objects.filter(username=options.get('username')).exists():

            try:
                User.objects.create_superuser(**options)

            except Exception as e:
                raise CommandError(e)

            self.stdout.write(
                    self.style.SUCCESS(
                        f"\nCreated admin user:\n\t\t{options['username']}\n\n"))
