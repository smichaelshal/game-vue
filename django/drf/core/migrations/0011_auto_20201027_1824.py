# Generated by Django 3.1.2 on 2020-10-27 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]