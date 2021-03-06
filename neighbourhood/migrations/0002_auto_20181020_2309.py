# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='kijiji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighbourhood.Kijiji'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='kijiji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='neighbourhood.Kijiji'),
        ),
        migrations.AlterField(
            model_name='news',
            name='kijiji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='neighbourhood.Kijiji'),
        ),
        migrations.AlterField(
            model_name='police',
            name='kijiji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='police', to='neighbourhood.Kijiji'),
        ),
    ]
