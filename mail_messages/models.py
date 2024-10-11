from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Клиент
class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


# Сообщение
class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'соббщение'
        verbose_name_plural = 'сообщения'


# Рассылка
class Mailing(models.Model):
    PERIODICITY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    title = models.CharField(max_length=100, default='Без названия', verbose_name='Название рассылки')
    start_datetime = models.DateTimeField(verbose_name='Дата и время первой рассылки')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f"{self.title} (ID: {self.id}) - {self.status}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


# Попытка рассылки
class MailingAttempt(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    attempt_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней рассылки')
    status = models.CharField(max_length=10, choices=[('success', 'Успешно'), ('failed', 'Неуспешно')], verbose_name='статус попытки')
    server_response = models.TextField(verbose_name='ответ почтового сервиса', **NULLABLE)

    def __str__(self):
        return f"Attempt for mailing {self.mailing.id} - {self.status}"

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
