# Generated by Django 3.0.4 on 2020-07-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsmain', '0015_auto_20200701_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
