from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def get_by_natural_key(self, username):
        return self.get(username=username)
    
    
class CustomUsers(AbstractBaseUser):
    email = models.EmailField('Email', unique=True, blank=True, null=True)
    username = models.CharField('Имя пользователя', max_length=50, unique=True, default='default_username')
    first_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    superlast_name = models.CharField('Отчество', max_length=50, blank=True)
    otdel = models.ForeignKey('Otdel', verbose_name='Отделение', max_length=256, on_delete=models.SET_NULL, null=True, blank=True)
    is_staff = models.BooleanField('Администратор', default=False)
    is_superuser = models.BooleanField('Суперпользователь', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_buh = models.BooleanField('Бухгалтерия', default=False)
    is_glav = models.BooleanField('Лидер', default=False)
    is_admin = models.BooleanField('Администрация', default=False)
    is_leed = models.BooleanField('Teamleed', default=False)
    deducted_amount = models.DecimalField('Списанные суммы', max_digits=10, decimal_places=2, default=0)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        # Ваша реализация проверки прав доступа
        return True

    def has_module_perms(self, app_label):
        # Ваша реализация проверки прав доступа к модулю
        return self.is_staff


class Otdel(models.Model):
    name = models.CharField('Название отделения', max_length=256)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name