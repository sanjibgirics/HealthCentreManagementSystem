# Generated by Django 3.0.4 on 2020-06-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsmain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
