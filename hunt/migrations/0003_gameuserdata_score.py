# Generated by Django 2.0.6 on 2018-06-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0002_auto_20180630_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameuserdata',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
