from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from apps.blog.models import Entry

class Command(BaseCommand):
    help = 'test command.'

    def handle(selef, **options):
        export_file = '/tmp/django_entries_%s.log' % datetime.now().strftime('%Y%m%d-%H%M%S')

        with open(export_file, 'w') as f:
            writer = csv.writer(f)
            entries = Entry.objects.all()

            for e in entries:
                writer.writerow([e.id, e.title, e.body, e.created_at, e.updated_at, e.status])

        print('export entries at %s' % export_file)
