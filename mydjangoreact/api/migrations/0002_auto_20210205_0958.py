# Generated by Django 3.1.6 on 2021-02-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='votes_to_skip',
            field=models.IntegerField(default=1),
        ),
    ]
