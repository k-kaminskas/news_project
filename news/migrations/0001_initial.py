# Generated by Django 2.1.5 on 2019-01-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('image_scr', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('votes', models.BigIntegerField()),
            ],
        ),
    ]
