# Generated by Django 4.1.6 on 2023-02-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
