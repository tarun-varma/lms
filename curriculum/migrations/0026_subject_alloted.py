# Generated by Django 3.1.7 on 2021-04-08 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0025_auto_20201012_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='alloted',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
