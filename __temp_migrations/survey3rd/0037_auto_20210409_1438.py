# Generated by Django 2.2.12 on 2021-04-09 12:38

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0036_auto_20210409_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s53_program_cd',
            field=otree.db.models.StringField(choices=[['progC', 'C: 400 mennesker vil omkomme med sikkerhed, de resterende 200 er for usikkert til at kunne komme med et estimat.'], ['progD', 'D: Der er en tredjedel sandsynlighed for, at ingen mennesker vil omkomme og to tredjedele for, \n at 600 vil omkomme. very long sentence no break']], max_length=10000, null=True),
        ),
    ]
