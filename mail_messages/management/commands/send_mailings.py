from django.core.management.base import BaseCommand
from mail_messages.tasks import send_mailing


class Command(BaseCommand):
    help = 'Send mailings manually'

    def handle(self, *args, **kwargs):
        send_mailing()
        self.stdout.write(self.style.SUCCESS('Mailings sent successfully!'))
