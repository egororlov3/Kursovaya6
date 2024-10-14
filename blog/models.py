from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog_images/', verbose_name='изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f"{self.title} - {self.content[:50]}..."