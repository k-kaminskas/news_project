# Generated by Django 2.1.5 on 2019-04-06 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190406_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvotes',
            name='user_id',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
