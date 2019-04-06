# Generated by Django 2.1.5 on 2019-03-29 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190329_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='alt_img',
            field=models.CharField(default='alt', max_length=50),
        ),
        migrations.AlterField(
            model_name='postvotes',
            name='user_id',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
