# Generated by Django 2.2.12 on 2021-03-09 09:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2nd', '0002_auto_20210309_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s61_movehouse',
            field=otree.db.models.StringField(choices=[['Not risky at all', 'Slet ikke risikofyldt'], ['Very little risk', 'Meget lidt risiko'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…flytte til et hus beliggende langs bredden af en flod'),
        ),
    ]
