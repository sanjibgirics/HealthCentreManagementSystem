# Generated by Django 3.0.4 on 2020-06-20 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hmsmain', '0003_auto_20200620_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='utype',
            field=models.CharField(max_length=30),
        ),
    ]
