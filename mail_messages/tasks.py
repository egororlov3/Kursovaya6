from django.utils import timezone
from django.core.mail import send_mail
from mail_messages.models import Mailing, MailingAttempt
import logging

logger = logging.getLogger(__name__)


def send_mailing():
    current_datetime = timezone.now()

    # Получаем рассылки, которые можно отправить
    mailings = Mailing.objects.filter(start_datetime__lte=current_datetime, status='started')

    for mailing in mailings:
        # Получаем последнюю попытку отправки для этой рассылки
        last_attempt = MailingAttempt.objects.filter(mailing=mailing).order_by('-attempt_datetime').first()

        if last_attempt:
            if mailing.periodicity == 'daily':
                if (current_datetime - last_attempt.attempt_datetime).days < 1:
                    continue

            elif mailing.periodicity == 'weekly':
                if (current_datetime - last_attempt.attempt_datetime).days < 7:
                    continue

            elif mailing.periodicity == 'monthly':
                if (current_datetime - last_attempt.attempt_datetime).days < 30:
                    continue

        # Логируем начало отправки
        logger.info(f"Обрабатываем рассылку: {mailing.title}")

        # Если условия выполнены, отправляем письма
        try:
            send_mail(
                subject=mailing.message.title,
                message=mailing.message.body,
                from_email='your_email@example.com',  # Укажите ваш email
                recipient_list=[client.email for client in mailing.clients.all()],
            )
            # Записываем успешную попытку
            MailingAttempt.objects.create(mailing=mailing, status='success')
            logger.info(f"Рассылка {mailing.title} успешно отправлена")
        except Exception as e:
            # Записываем неудачную попытку
            MailingAttempt.objects.create(mailing=mailing, status='failed', server_response=str(e))
            logger.error(f"Ошибка при отправке рассылки {mailing.title}: {e}")

    logger.info("Завершена отправка рассылок")
