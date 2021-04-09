# Generated by Django 2.2.12 on 2021-04-09 08:50

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0023_auto_20210409_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s52_program_ab',
            field=otree.db.models.StringField(choices=[['progA', 'Scenarie A: 200 mennesker bliver reddet med sikkerhed, de resterende 400 er for usikkert til at kunne komme med et estimat.'], ['progB', 'Scenarie B: Der er en tredjedel (33,3%) sandsynlighed for, at 600 mennesker bliver reddet, og to tredjedels (66,6%) sandsynlighed for, at ingen mennesker bliver reddet.']], max_length=10000, null=True),
        ),
    ]