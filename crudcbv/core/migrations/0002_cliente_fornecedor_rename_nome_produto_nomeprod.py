# Generated by Django 4.1.6 on 2023-02-08 15:38

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomeClie", models.CharField(max_length=100)),
                (
                    "telefoneClie",
                    models.CharField(
                        max_length=11, validators=[core.models.validate_telefone]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomeForn", models.CharField(max_length=100)),
                (
                    "telefoneForn",
                    models.CharField(
                        max_length=11, validators=[core.models.validate_telefone]
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="produto", old_name="nome", new_name="nomeProd",
        ),
    ]
