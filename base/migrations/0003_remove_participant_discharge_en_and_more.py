# Generated by Django 4.2.1 on 2023-06-02 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_city_profile_organization_profile_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='discharge_en',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='discharge_ru',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fullName_en',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fullName_ru',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userType_en',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userType_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='about_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='about_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='chiefJustice_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='chiefJustice_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='chiefSecretary_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='chiefSecretary_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='credit_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='credit_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='place_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='place_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='rang_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='rang_ru',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='weightcategory',
            name='gender_en',
        ),
        migrations.RemoveField(
            model_name='weightcategory',
            name='gender_ru',
        ),
    ]
