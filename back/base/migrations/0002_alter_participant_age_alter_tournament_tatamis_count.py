# Generated by Django 4.1.7 on 2023-04-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tatamis_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]