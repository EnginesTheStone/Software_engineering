# Generated by Django 5.1.6 on 2025-02-20 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mycards",
            old_name="cardName",
            new_name="cardname",
        ),
        migrations.RenameField(
            model_name="mycards",
            old_name="cardPrice",
            new_name="cardprice",
        ),
    ]
