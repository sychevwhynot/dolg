# Generated by Django 4.2.13 on 2024-06-13 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название отделения')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(default='default_username', max_length=50, unique=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('superlast_name', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_buh', models.BooleanField(default=False, verbose_name='Бухгалтерия')),
                ('is_glav', models.BooleanField(default=False, verbose_name='Лидер')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Палач')),
                ('deducted_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Списанные суммы')),
                ('otdel', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.otdel', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]