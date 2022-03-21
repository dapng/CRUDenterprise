from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', null=True, blank=True)
    info = models.CharField('Участники', max_length=200, null=True, blank=True)
    link = models.URLField('Ссылка', max_length=200, null=True, blank=True)
    last_date = models.DateTimeField('Дата окончания', null=True, blank=True, default=datetime.datetime.today)
    complete = models.BooleanField('Выполнено', default=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
