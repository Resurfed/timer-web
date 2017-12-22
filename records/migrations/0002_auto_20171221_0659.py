# Generated by Django 2.0 on 2017-12-21 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapconfiguration',
            name='map',
        ),
        migrations.AlterUniqueTogether(
            name='spawn',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='spawn',
            name='map',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='map',
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maps.Map'),
        ),
        migrations.AlterField(
            model_name='time',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maps.Map'),
        ),
        migrations.DeleteModel(
            name='Map',
        ),
        migrations.DeleteModel(
            name='MapConfiguration',
        ),
        migrations.DeleteModel(
            name='Spawn',
        ),
        migrations.DeleteModel(
            name='Zone',
        ),
    ]
