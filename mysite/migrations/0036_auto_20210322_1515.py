# Generated by Django 3.1.4 on 2021-03-22 15:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0035_auto_20210319_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 15, 15, 55, 331595, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='post',
            field=models.CharField(choices=[(0, 'Convener'), (1, 'Joint Convener'), (2, 'President'), (3, 'Vice President'), (4, 'Secretary'), (5, 'Chair'), (6, 'Website Head'), (7, 'Chief Co-ordinator'), (8, 'Public Relations Head'), (9, 'Executive Member')], default=[(0, 'Convener'), (1, 'Joint Convener'), (2, 'President'), (3, 'Vice President'), (4, 'Secretary'), (5, 'Chair'), (6, 'Website Head'), (7, 'Chief Co-ordinator'), (8, 'Public Relations Head')], max_length=50),
        ),
    ]