# Generated by Django 2.1.2 on 2018-10-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadnode',
            name='chunk',
        ),
        migrations.AddField(
            model_name='chunk',
            name='road_nodes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RoadNode',
        ),
    ]
