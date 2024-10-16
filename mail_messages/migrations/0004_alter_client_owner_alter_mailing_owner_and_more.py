# Generated by Django 5.1.1 on 2024-10-12 20:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_messages', '0003_client_owner_mailing_owner_message_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AlterField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
    ]
