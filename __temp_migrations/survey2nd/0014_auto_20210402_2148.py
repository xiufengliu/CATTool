# Generated by Django 2.2.12 on 2021-04-02 19:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2nd', '0013_auto_20210402_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name='E-mail:'),
        ),
    ]