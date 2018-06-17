# Generated by Django 2.1a1 on 2018-06-17 15:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 6, 17, 15, 51, 44, 326639, tzinfo=utc))),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]