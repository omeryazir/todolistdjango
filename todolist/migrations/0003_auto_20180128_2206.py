# Generated by Django 2.0.1 on 2018-01-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20180128_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
