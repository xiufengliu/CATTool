# Generated by Django 2.2.12 on 2021-04-09 08:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0021_auto_20210409_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=otree.db.models.StringField(blank=True, default='', max_length=10000, null=True),
        ),
    ]