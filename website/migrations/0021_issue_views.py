# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-04 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_issue_user_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]