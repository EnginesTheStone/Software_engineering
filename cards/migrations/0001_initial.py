# Generated by Django 5.1.6 on 2025-02-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardName', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=50)),
                ('cardType', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('manaCost', models.CharField(max_length=10)),
                ('cardPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cardGuild', models.CharField(max_length=10)),
                ('cardSet', models.CharField(max_length=10)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
