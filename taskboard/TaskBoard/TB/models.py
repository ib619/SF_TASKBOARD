from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from .choices import DECISION_TYPE


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('trader', 'Торговцы'),
        ('gm', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('leather', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spell', 'Мастера Заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=20, choices=TYPE, default='tank')
    text = RichTextUploadingField()
    video = models.FileField(upload_to='videos', blank=True, null=True, verbose_name='Upload First Video:')
    video2 = models.FileField(upload_to='videos', blank=True, null=True, verbose_name='Upload Second Video:')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return '/articles/'

    def __str__(self):
        return f'{self.title}'

    def get_category(self):
        my_category = self.get_category_display()
        return my_category


class Response(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    decision = models.CharField(max_length=20, choices=DECISION_TYPE, default='undecided')

    def __str__(self):
        return f'{self.author.username}: {self.text[0:40]}'

    def get_decision(self):
        my_decision = self.get_decision_display()
        return my_decision






