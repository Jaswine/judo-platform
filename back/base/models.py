from django.db import models
from django.contrib.auth.models import User

# Auto Add
class Profile(models.Model):
   TASKS = (
      ('Админ', 'Админ'),
      ('Секретарь', 'Секретарь'),
      ('Свободный', 'Свободный')
   )
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   fullName = models.CharField(max_length=100, blank=True)
   phone = models.CharField(max_length=12, blank=True)
   userType = models.CharField(max_length=20, choices=TASKS)
   image = models.ImageField(upload_to='profile_avatars', blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   
# Logotips Gallery
class Logos(models.Model):
   image = models.FileField(upload_to='tournaments_logos')
   
   def __str__(self):
      return self.image
   
# Weight Category
class WeightCategory(models.Model):
   category = models.CharField(max_length=20, blank=True)
   gender = models.CharField(max_length=20, blank=True)
   weight = models.CharField(max_length=100, blank=True)
   year = models.CharField(max_length=20, blank=True)
   
   def __str__(self):
      return self.category 

# Sponsors Emblems or Names
class Sponsors(models.Model):
   name = models.CharField(max_length=100,blank=True)
   image = models.ImageField(upload_to='sponsors', blank=True)

# Participants
class Participant(models.Model):
   fullName = models.CharField(max_length=100)
   data = models.CharField(max_length=30, blank=True)
   discharge = models.CharField(max_length=10, blank=True)
   comand = models.CharField(max_length=40, blank=True)
   country = models.CharField(max_length=20, blank=True)
   weightCategory = models.ForeignKey(WeightCategory, on_delete=models.CASCADE, blank=True)
   weight = models.CharField(max_length=100, blank=True)
   age = models.IntegerField(blank=True)
   trainer = models.CharField(max_length=100, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.fullName
   
# Tournir
class Tournament(models.Model):

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
   
   user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=100, unique=True)
   logos = models.ManyToManyField(Logos, default=[], blank=True)
   about = models.TextField(max_length=1000, blank=True)
   
   rang = models.CharField(max_length=40,choices=RANGS, blank=True)
   
   country = models.CharField(max_length=100, blank=True)
   city = models.CharField(max_length=100, blank=True)
   address = models.CharField(max_length=100, blank=True)
   place = models.CharField(max_length=100, blank=True)
   
   startData = models.CharField(max_length=100, blank=True)
   finishData = models.CharField(max_length=100, blank=True)

   credit = models.CharField(max_length=100, blank=True, choices=CREDIT_TYPE)
   
   tatamis_count = models.IntegerField(default=0, blank=True)
   
   weight_categories = models.ManyToManyField(WeightCategory, blank=True, default=[])
   sponsors = models.ManyToManyField(Sponsors, blank=True, default=[])
   
   chiefJustice = models.CharField(max_length=200, blank=True)
   chiefSecretary = models.CharField(max_length=200, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   class Meta: 
      ordering = ['-updated', '-created']
   
   def __str__(self):
      return self.title