# Generated by Django 3.2.1 on 2021-05-12 15:01

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoFence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('raw_geo_fence', models.TextField()),
                ('upper_limit', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lower_limit', models.DecimalField(decimal_places=2, max_digits=4)),
                ('altitude_ref', models.IntegerField(choices=[(0, 'WGS84'), (1, 'AGL'), (2, 'MSL')], default=0)),
                ('name', models.CharField(max_length=50)),
                ('bounds', models.CharField(max_length=140)),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('end_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
