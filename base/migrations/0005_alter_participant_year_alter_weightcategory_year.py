# Generated by Django 4.2.7 on 2024-01-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_weightcategory_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='year',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='weightcategory',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]