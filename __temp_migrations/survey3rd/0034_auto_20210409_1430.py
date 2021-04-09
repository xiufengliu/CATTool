# Generated by Django 2.2.12 on 2021-04-09 12:30

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0033_auto_20210409_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s61_findsolution',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s62_findvalue',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s63_understand_issue',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
    ]