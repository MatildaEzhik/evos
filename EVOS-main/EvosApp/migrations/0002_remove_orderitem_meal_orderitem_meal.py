# Generated by Django 4.2.14 on 2024-09-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvosApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='meal',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='meal',
            field=models.ManyToManyField(to='EvosApp.meal'),
        ),
    ]
