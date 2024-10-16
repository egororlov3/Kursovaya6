# Generated by Django 5.1.1 on 2024-10-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked',
            field=models.BooleanField(default=False, verbose_name='блокировка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='верификация'),
        ),
    ]
