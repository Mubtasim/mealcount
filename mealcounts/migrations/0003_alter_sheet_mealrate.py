# Generated by Django 3.2 on 2021-05-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealcounts', '0002_sheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='mealRate',
            field=models.FloatField(null=True),
        ),
    ]