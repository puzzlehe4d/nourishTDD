# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0004_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(to='fridges.Store', default=None),
        ),
    ]
