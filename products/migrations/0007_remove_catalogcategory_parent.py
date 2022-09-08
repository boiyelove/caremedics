# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogcategory',
            name='parent',
        ),
    ]
