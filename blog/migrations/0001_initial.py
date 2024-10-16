# Generated by Django 5.1.1 on 2024-10-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое статьи')),
                ('image', models.ImageField(upload_to='blog_images/', verbose_name='изображение')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
        ),
    ]
