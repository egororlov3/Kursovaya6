# Generated by Django 5.1.1 on 2024-10-14 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_block_users', 'Can block users')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
