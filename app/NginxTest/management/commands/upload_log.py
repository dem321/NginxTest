from django.core.management import BaseCommand

from log_module.utils import process_file_from_url


class Command(BaseCommand):
    help = 'Upload logs from nginx log file using url'

    def add_arguments(self, parser):
        parser.add_argument('file_url', type=str)

    def handle(self, *args, **options):
        errors = process_file_from_url(options['file_url'])
        if errors:
            self.stdout.write(self.style.ERROR(errors))
        else:
            self.stdout.write(
                self.style.SUCCESS('Successfully uploaded logs')
            )
