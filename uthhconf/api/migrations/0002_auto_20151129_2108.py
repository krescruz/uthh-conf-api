# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.CharField(max_length=15)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('privado', models.BooleanField(default=False)),
                ('equipo', models.ForeignKey(to='api.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comentarios',
            name='equipo',
        ),
        migrations.DeleteModel(
            name='Comentarios',
        ),
    ]
