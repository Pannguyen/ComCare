# Generated by Django 4.2.5 on 2023-10-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='anonyme',
            field=models.BooleanField(default=False),
        ),
    ]