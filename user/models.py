from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    """
        Профиль пользователя
    """
    TASKS = (
        ('Админ', 'Админ'),
        ('Секретарь', 'Секретарь'),
        ('Свободный', 'Свободный')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    fullName = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, blank=True)

    organization = models.CharField(max_length=300, blank=True)

    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)

    userType = models.CharField(max_length=20, choices=TASKS, default='Свободный')

    def avatar_directory_path(instance, filename) -> str:
        username = instance.user.username if instance.user else 'unknown_user'
        extension = filename.split('.')[-1]
        new_filename = f'{username}_document_{uuid.uuid4().hex[:10]}.{extension}'
        return f'uploads/users/{username}/avatars/{new_filename}'

    image = models.ImageField(upload_to=avatar_directory_path, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Participant(models.Model):
    """
        Участник
    """
    EVENT_FUNCTIONS = (
        ('Спортсмен', 'Спортсмен'),
        ('Тренер', 'Тренер'),
        ('Судья', 'Судья'),
    )

    JUDGE_TYPE = (
        ('Судейско-вспомогательный персонал', 'Судейско-вспомогательный персонал'),
        ('Арбитр', 'Арбитр'),
        ('Информатор', 'Информатор'),
        ('Секретариат', 'Секретариат'),
        ('Судейская комиссия', 'Судейская комиссия'),
        ('Руководитель татами (комиссар)', 'Руководитель татами (комиссар)'),
        ('Главный секретарь', 'Главный секретарь'),
        ('Главный судья', 'Главный судья'),
    )

    GENDER = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    )

    DISCHARGES = (
        ('Белый пояс (мукю)', 'Белый пояс (мукю)'),
        ('Желтый пояс (10 кю)', 'Желтый пояс (10 кю)'),
        ('Оранжевый пояс (9 кю)', 'Оранжевый пояс (9 кю)'),
        ('Зеленый пояс (8 кю)', 'Зеленый пояс (8 кю)'),
        ('Синий пояс (7 кю)', 'Синий пояс (7 кю)'),
        ('Коричневый пояс (6 кю - 1 кю)', 'Коричневый пояс (6 кю - 1 кю)'),
        ('Черный пояс (1 дан - 10 дан)', 'Черный пояс (1 дан - 10 дан)'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    thirdName = models.CharField(max_length=100, blank=True)

    def participant_directory_path(instance, filename) -> str:
        username = instance.user.username if instance.user else 'unknown_user'
        fio = f'{instance.firstName} {instance.lastName} {instance.thirdName}'

        extension = filename.split('.')[-1]
        new_filename = f'{username}_document_{uuid.uuid4().hex[:10]}.{extension}'

        return f'uploads/users/{username}/participants/{fio}/images/{new_filename}'

    event_function = models.CharField(max_length=10, choices=EVENT_FUNCTIONS)

    ava = models.ImageField(upload_to=participant_directory_path, blank=True)

    year = models.DateField(null=True, blank=True)
    discharge = models.CharField(max_length=40, choices=DISCHARGES, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    coach = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, related_name='sports_coach')
    judge_type = models.CharField(max_length=40, choices=JUDGE_TYPE, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.firstName, self.lastName, self.thirdName)
