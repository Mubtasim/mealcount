# Generated by Django 3.2 on 2021-05-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealcounts', '0006_remove_member_khoroch'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
