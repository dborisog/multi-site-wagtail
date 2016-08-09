# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-09 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_auto_20160728_2020'),
        ('standard_page', '0002_auto_20160728_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherHomePage',
            fields=[
                ('homepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.HomePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.homepage',),
        ),
        migrations.CreateModel(
            name='AnotherStandardPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='standard_page.StandardPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('standard_page.standardpage',),
        ),
    ]
