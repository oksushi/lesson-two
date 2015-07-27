# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20150727_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(to='entries.Client'),
        ),
    ]
