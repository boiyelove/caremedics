# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_catalogcategory_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='img/products', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(upload_to='img/products'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
