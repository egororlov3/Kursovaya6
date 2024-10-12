from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_messages'

    def ready(self):
        from .tasks import send_mailing  # Переместите импорт сюда
        scheduler = BackgroundScheduler()
        scheduler.add_job(send_mailing, 'interval', seconds=60)  # Запускать каждые 60 секунд
        scheduler.start()
