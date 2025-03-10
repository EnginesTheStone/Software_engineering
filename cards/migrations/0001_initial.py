# Generated by Django 5.1.6 on 2025-02-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="myCards",
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
                ("cardName", models.CharField(max_length=100)),
                ("cardPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField()),
                (
                    "cardimage",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
            options={
                "verbose_name_plural": "myCards",
            },
        ),
    ]
