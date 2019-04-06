# Generated by Django 2.1.5 on 2019-02-15 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(default='red', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('rss', models.CharField(max_length=250)),
                ('score', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=150)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.PostCategory')),
            ],
        ),
        migrations.RenameField(
            model_name='newspost',
            old_name='link',
            new_name='article_link',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='source',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='votes',
        ),
        migrations.AddField(
            model_name='newspost',
            name='down_votes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newspost',
            name='ext_id',
            field=models.CharField(default='ext_id', max_length=250),
        ),
        migrations.AddField(
            model_name='newspost',
            name='text',
            field=models.TextField(default='Article text'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='up_votes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='newspost',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.PostCategory'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='source_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Source'),
        ),
    ]
