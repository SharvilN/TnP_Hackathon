# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-12 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170212_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='title',
            field=models.CharField(choices=[('Mrs', 'Mrs.'), ('Ms', 'Ms.'), ('Mr', 'Mr.')], max_length=4),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='branch',
            field=models.CharField(choices=[('MIN', 'Mining'), ('CIV', 'Civil Engineering'), ('MECH', 'Mechanical Engineering'), ('META', 'Metallurgy'), ('ARCH', 'Architecture'), ('CHEM', 'Chemical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CSE', 'Computer Science & Engineering')], max_length=4),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='enr_no',
            field=models.IntegerField(null=True),
        ),
    ]