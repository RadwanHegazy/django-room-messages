# Generated by Django 4.2.5 on 2023-09-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='key',
        ),
    ]