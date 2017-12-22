from django.db import models


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=60, blank=True)
    date_created = models.DateTimeField()
    current_map = models.CharField(max_length=50, blank=True)
    bots_enabled = models.IntegerField()
    key = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Time(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('maps.Map', on_delete=models.PROTECT)
    player = models.ForeignKey('users.Player', on_delete=models.PROTECT)
    type = models.SmallIntegerField()
    stage = models.SmallIntegerField()
    time = models.FloatField()
    rank = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    server = models.ForeignKey(Server, on_delete=models.PROTECT)
    completions = models.IntegerField()
    best_rank = models.IntegerField()
    date_demoted = models.DateTimeField()

    class Meta:
        unique_together = (('map', 'player', 'stage', 'type'),)
        index_together = (('map', 'type', 'stage'),)

    def __str__(self):
        return "%s - %s (Type: %s, Stage: %s)" % (self.player, self.map, self.type, self.stage)


class Checkpoint(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey('users.Player', on_delete=models.PROTECT)
    map = models.ForeignKey('maps.Map', on_delete=models.PROTECT)
    zone = models.SmallIntegerField()
    time = models.FloatField()
    stage_time = models.FloatField()
    velocity = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = (('player', 'map', 'zone'),)
