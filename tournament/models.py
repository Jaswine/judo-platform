from django.db import models
from django.contrib.auth.models import User

from user.models import Participant


class Tournament(models.Model):
    """
        Турнир
    """
    RANGS = (
        ('Клубный', 'Клубный'),
        ('Городской', 'Городской'),
        ('Областной', 'Областной'),
        ('Региональный', 'Региональный'),
        ('Республиканский', 'Республиканский'),
        ('Чемпионат РК', 'Чемпионат РК'),
        ('Международный турнир', 'Международный турнир'),
    )

    CREDIT_TYPE = (
        ('личный', 'личный'),
        ('командный', 'командный')
    )

    STATUS = (
        ('Регистрация открыта', 'Регистрация открыта'),
        ('Регистрация завершенa', 'Регистрация завершенa'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    title = models.CharField(max_length=300, verbose_name='Title')
    slug = models.SlugField(max_length=300, unique=True, default='')
    logo = models.ImageField(upload_to='tournament_logo', blank=True)
    logos = models.ManyToManyField('Logos', default=[], blank=True, related_name='logos')
    about = models.TextField(max_length=3000, blank=True)

    rang = models.CharField(max_length=40, choices=RANGS, blank=True)

    place = models.CharField(max_length=100, blank=True)

    startData = models.DateField(max_length=100, blank=True)
    finishData = models.DateField(max_length=100, blank=True)
    startTime = models.TimeField(max_length=10, blank=True)

    credit = models.CharField(max_length=100, blank=True, choices=CREDIT_TYPE)

    tatamis_count = models.CharField(default=0, blank=True, max_length=2)

    sponsors = models.ManyToManyField('Sponsors', blank=True, default=[], related_name='sponsors')

    chiefJustice = models.CharField(Participant, on_delete=models.CASCADE, blank=True)
    chiefSecretary = models.CharField(Participant, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='Регистрация_открыта')

    public = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Weight(models.Model):
    """
        Вес
    """
    name = models.CharField(max_length=10)
    sorting = models.JSONField(blank=True, null=True)

    participants = models.ManyToManyField(Participant, default=[], blank=True)

    def __str__(self):
        return self.name

class WeightCategory(models.Model):
    """
        Весовая категория
    """
    GENDER = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    )

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True)
    weight = models.ManyToManyField(Weight, default=[])

    year = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)

    def delete(self):
        weights = self.weight.all()

        for w in weights:
            w.delete()

        super(WeightCategory, self).delete()

    def __str__(self):
        return self.year


class Logos(models.Model):
    """
        Логотипы турниров
    """
    image = models.ImageField(upload_to='tournaments_logos')

    def __str__(self):
        return self.image.name


class Sponsors(models.Model):
    """
        Спонсоры турниров
    """
    image = models.ImageField(upload_to='sponsors', blank=True)

    def __str__(self):
        return self.image.name