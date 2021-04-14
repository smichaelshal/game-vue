# Generated by Django 3.1.2 on 2020-10-28 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_auto_20201028_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.numberrange')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
