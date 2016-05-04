# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(serialize=False, primary_key=True, max_length=254)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', verbose_name='groups', related_query_name='user', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', blank=True, to='auth.Permission', verbose_name='user permissions', related_query_name='user', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
