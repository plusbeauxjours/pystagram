# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pystagram.file
import pystagram.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(validators=[pystagram.validators.jpeg_validator], blank=True, upload_to=pystagram.file.random_name_with_file_field, null=True),
        ),
    ]
