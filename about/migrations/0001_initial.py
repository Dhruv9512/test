# Generated by Django 5.1 on 2024-12-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("Name", models.CharField(max_length=100)),
                ("institution", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("status", models.CharField(max_length=100)),
                ("score", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("Name", models.CharField(max_length=150)),
                ("skill", models.CharField(max_length=255)),
                ("Proficiency", models.CharField(max_length=100)),
            ],
        ),
    ]