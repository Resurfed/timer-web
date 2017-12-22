# Generated by Django 2.0 on 2017-12-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone', models.SmallIntegerField()),
                ('time', models.FloatField()),
                ('stage_time', models.FloatField()),
                ('velocity', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('type', models.IntegerField()),
                ('checkpoints', models.SmallIntegerField()),
                ('bonuses', models.SmallIntegerField()),
                ('difficulty', models.SmallIntegerField()),
                ('prevent_prehop', models.SmallIntegerField()),
                ('enable_baked_triggers', models.BooleanField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('date_created', models.DateTimeField()),
                ('current_map', models.CharField(blank=True, max_length=50)),
                ('bots_enabled', models.IntegerField()),
                ('key', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Spawn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone', models.SmallIntegerField()),
                ('type', models.SmallIntegerField()),
                ('origin', models.CharField(max_length=80)),
                ('angle', models.CharField(max_length=80)),
                ('velocity', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField()),
                ('stage', models.SmallIntegerField()),
                ('time', models.FloatField()),
                ('rank', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('completions', models.IntegerField()),
                ('best_rank', models.IntegerField()),
                ('date_demoted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.CharField(max_length=80)),
                ('end', models.CharField(max_length=80)),
                ('type', models.IntegerField()),
                ('value', models.IntegerField()),
                ('limit_speed', models.BooleanField()),
                ('target_name', models.CharField(blank=True, max_length=32)),
                ('filter_name', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MapConfiguration',
            fields=[
                ('map', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='records.Map')),
                ('config', models.CharField(blank=True, max_length=20000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='zone',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Map'),
        ),
        migrations.AddField(
            model_name='time',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='records.Map'),
        ),
        migrations.AddField(
            model_name='time',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Player'),
        ),
        migrations.AddField(
            model_name='time',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='records.Server'),
        ),
        migrations.AddField(
            model_name='spawn',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Map'),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='records.Map'),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='time',
            unique_together={('map', 'player', 'stage', 'type')},
        ),
        migrations.AlterIndexTogether(
            name='time',
            index_together={('map', 'type', 'stage')},
        ),
        migrations.AlterUniqueTogether(
            name='spawn',
            unique_together={('map', 'zone', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='checkpoint',
            unique_together={('player', 'map', 'zone')},
        ),
    ]
