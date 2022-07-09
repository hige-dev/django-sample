from django.core.management.base import BaseCommand
from blog.models import Entry

class Command(BaseCommand):
    help = 'test command.'

    def add_arguments(self, parser):
        parser.add_argument('entry_ids', nargs='+', type=int)

    def handle(selef, *args, **options):
        for entry_id in options['entry_ids']:
            try:
                entry = Entry.objects.get(pk=entry_id)
                print(entry.title)
            except Entry.DoesNotExist:
                raise CommandError("Entry %s does not exist" % entry_id)
