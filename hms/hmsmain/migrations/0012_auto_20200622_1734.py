# Generated by Django 3.0.4 on 2020-06-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsmain', '0011_auto_20200622_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=2, null=True),
        ),
    ]
