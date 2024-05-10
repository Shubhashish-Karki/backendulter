# Generated by Django 4.1.13 on 2024-05-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0004_remove_sensordata_timestamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="MediaContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="videos/")),
                ("photo", models.ImageField(upload_to="photos/")),
            ],
            options={
                "verbose_name_plural": "Media Content",
            },
        ),
    ]
