# Generated by Django 4.2.1 on 2023-06-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("First_Name", models.CharField(max_length=126)),
                ("Last_Name", models.CharField(max_length=126)),
                ("email", models.CharField(max_length=126, unique=True)),
            ],
        ),
    ]
