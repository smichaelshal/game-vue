# Generated by Django 3.1.2 on 2020-10-28 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_life_numberrange'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Life',
        ),
        migrations.DeleteModel(
            name='NumberRange',
        ),
    ]
