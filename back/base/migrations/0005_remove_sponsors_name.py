# Generated by Django 4.1.7 on 2023-04-11 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_weightcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsors',
            name='name',
        ),
    ]