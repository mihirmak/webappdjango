# Generated by Django 2.1 on 2018-08-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockoverflow', '0005_auto_20180828_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='userid',
            field=models.IntegerField(max_length=20),
        ),
    ]