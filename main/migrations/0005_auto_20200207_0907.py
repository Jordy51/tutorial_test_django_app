# Generated by Django 3.0.2 on 2020-02-07 09:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200207_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 7, 9, 964142), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_series', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('tutorial_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
    ]
