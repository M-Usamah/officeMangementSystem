# Generated by Django 4.2.5 on 2023-09-18 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employdetails',
            old_name='moddle_name',
            new_name='middle_name',
        ),
    ]