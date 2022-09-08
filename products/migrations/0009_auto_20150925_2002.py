# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150925_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/products', null=True),
        ),
    ]
