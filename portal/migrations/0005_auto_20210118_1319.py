# Generated by Django 3.1.4 on 2021-01-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20210118_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='datOfBirth',
            field=models.DateField(),
        ),
    ]
