# Generated by Django 4.1.13 on 2024-05-10 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_sensordata_delete_todo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sensordata",
            name="timestamp",
        ),
    ]
