# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('message', models.TextField(verbose_name='change message', blank=True)),
                ('creator_ip', models.IPAddressField(verbose_name='creator ip')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'ordering': ['-modified'],
                'verbose_name_plural': 'Revisions',
                'verbose_name': 'Revision',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(verbose_name='slug', max_length=255)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name_plural': 'Wiki pages',
                'verbose_name': 'Wiki page',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='revision',
            name='page',
            field=models.ForeignKey(to='wakawaka.WikiPage'),
            preserve_default=True,
        ),
    ]
