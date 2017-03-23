# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 18:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.BooleanField(default=True)),
                ('response', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('display_name', models.CharField(blank=True, max_length=3)),
                ('notifications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Notifications')),
                ('petitions_created', models.ManyToManyField(blank=True, related_name='profile_petitions_created', to='petitions.Petition')),
                ('petitions_signed', models.ManyToManyField(blank=True, related_name='profile_petitions_signed', to='petitions.Petition')),
                ('subscriptions', models.ManyToManyField(blank=True, related_name='profile_subscriptions', to='petitions.Petition')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
