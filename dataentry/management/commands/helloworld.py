from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints Hello World"
    
    def handle(self, *args, **kwargs):
        # we write a logic
        self.stdout.write('Hello World')