# Generated by Django 2.0.7 on 2018-07-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0002_auto_20180721_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]