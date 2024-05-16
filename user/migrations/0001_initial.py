# Generated by Django 5.0.6 on 2024-05-16 05:10

import django.db.models.deletion
import user.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fullName', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('organization', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('userType', models.CharField(choices=[('Админ', 'Админ'), ('Секретарь', 'Секретарь'), ('Свободный', 'Свободный')], default='Свободный', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to=user.models.Profile.avatar_directory_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('thirdName', models.CharField(blank=True, max_length=100)),
                ('event_function', models.CharField(choices=[('Спортсмен', 'Спортсмен'), ('Тренер', 'Тренер'), ('Судья', 'Судья')], max_length=10)),
                ('ava', models.ImageField(blank=True, upload_to=user.models.Participant.participant_directory_path)),
                ('year', models.DateField(blank=True, null=True)),
                ('discharge', models.CharField(blank=True, choices=[('Белый пояс (мукю)', 'Белый пояс (мукю)'), ('Желтый пояс (10 кю)', 'Желтый пояс (10 кю)'), ('Оранжевый пояс (9 кю)', 'Оранжевый пояс (9 кю)'), ('Зеленый пояс (8 кю)', 'Зеленый пояс (8 кю)'), ('Синий пояс (7 кю)', 'Синий пояс (7 кю)'), ('Коричневый пояс (6 кю - 1 кю)', 'Коричневый пояс (6 кю - 1 кю)'), ('Черный пояс (1 дан - 10 дан)', 'Черный пояс (1 дан - 10 дан)')], max_length=40)),
                ('gender', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=10)),
                ('judge_type', models.CharField(blank=True, choices=[('Судейско-вспомогательный персонал', 'Судейско-вспомогательный персонал'), ('Арбитр', 'Арбитр'), ('Информатор', 'Информатор'), ('Секретариат', 'Секретариат'), ('Судейская комиссия', 'Судейская комиссия'), ('Руководитель татами (комиссар)', 'Руководитель татами (комиссар)'), ('Главный секретарь', 'Главный секретарь'), ('Главный судья', 'Главный судья')], max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('coach', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sports_coach', to='user.participant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
