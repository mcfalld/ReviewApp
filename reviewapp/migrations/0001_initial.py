# Generated by Django 2.0.7 on 2018-07-21 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('body', models.TextField(max_length=10000)),
                ('ipAddress', models.GenericIPAddressField()),
                ('submitted_on', models.DateTimeField(default=datetime.datetime.now)),
                ('company', models.CharField(max_length=200)),
                ('reviewerData', models.EmailField(max_length=250)),
            ],
        ),
    ]