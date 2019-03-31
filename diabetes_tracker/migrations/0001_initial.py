# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glucose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('glucose', models.IntegerField()),
                ('sleep', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('duration_of_exercise', models.IntegerField()),
                ('type_of_exercise', models.CharField(max_length=128)),
            ],
        ),
    ]
