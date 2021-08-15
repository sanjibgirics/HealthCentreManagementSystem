# Generated by Django 3.0.4 on 2020-07-01 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsmain', '0013_order_lastcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientID', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('dateIssued', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='consumptionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmqty', models.IntegerField(default=0, null=True)),
                ('cmid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmid', to='hmsmain.Medicine')),
                ('coid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comsumption_id', to='hmsmain.Consumption')),
            ],
        ),
    ]
