# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-16 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180413_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=100)),
                ('playerScore', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=100)),
                ('teamScore', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='playerTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Team'),
        ),
    ]
