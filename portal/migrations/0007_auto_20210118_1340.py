# Generated by Django 3.1.4 on 2021-01-18 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20210118_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='datofBirth',
            new_name='birthDate',
        ),
    ]
