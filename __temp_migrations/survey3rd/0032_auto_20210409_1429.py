# Generated by Django 2.2.12 on 2021-04-09 12:29

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0031_auto_20210409_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s210_gettouchstranger',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s211_worry',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s212_wondering',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s213_goodimg',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s214_precise',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s215_agreeothers',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s216_talkothers',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s217_overcome',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s218_famous',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s219_lovepeople',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s21_lookpainting',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s220_dothings',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s221_staycalm',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s222_wellmanner',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s223_tear',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s224_soap',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s22_thingsinplace',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s23_remainunkind',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s24_nobodylikeme',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s25_afraidfeelingpain',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s26_hardtolie',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s27_sciboring',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s28_postponetask',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='s29_criticism',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
    ]