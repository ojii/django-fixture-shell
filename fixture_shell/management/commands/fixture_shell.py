from __future__ import with_statement
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.commands import shell
from django.db import connections


FIXTURE_SHELL_DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:'
}


class Command(BaseCommand):
    option_list = shell.Command.option_list 
    def handle(self, filename, *app_labels, **options):
        connections.databases['default'] = FIXTURE_SHELL_DB
        call_command('syncdb', migrate_all=True, interactive=False, verbosity=0)
        call_command('shell', **options)
        with open(filename, 'wb') as fobj:
            call_command('dumpdata', *app_labels, stdout=fobj)