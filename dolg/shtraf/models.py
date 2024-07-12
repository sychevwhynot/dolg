from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Shtraf(models.Model):
    summa = models.IntegerField('Сумма штрафа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField('Дата наложения штрафа', auto_now_add=True)
    reason = models.CharField('Причина: ', max_length=255, default='Нет комментария')

    class Meta:
        verbose_name = 'Штраф'
        verbose_name_plural = 'Штрафы'

    def __str__(self):
        return self.reason
    
class Spisanie(models.Model):
    summa = models.IntegerField('Сумма штрафа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField('Дата наложения штрафа', auto_now_add=True)
    reason = models.CharField('Причина: ', max_length=255, default='Нет комментария')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Списание'
        verbose_name_plural = 'Списания'

    def __str__(self):
        return self.reason
