# Generated by Django 3.2.3 on 2021-06-22 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20210623_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
    ]
