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

    TIME_TYPE_CHOICES = (
        ('M', 'Map'),
        ('B', 'Bonus'),
    )

    type = models.CharField(max_length=1, choices=TIME_TYPE_CHOICES)
    stage = models.SmallIntegerField()
    time = models.FloatField()
    rank = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    server = models.ForeignKey(Server, on_delete=models.PROTECT)
    completions = models.IntegerField(blank=True, default=1)
    best_rank = models.IntegerField(blank=True, null=True)
    date_demoted = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (('map', 'player', 'stage', 'type'),)
        index_together = (('map', 'type', 'stage'),)

    def __str__(self):
        return "%s - %s (Type: %s, Stage: %s)" % (self.player, self.map, self.type, self.stage)

    def actual_rank(self):

        # as an optimization, only the top 10 best times are ranked
        if self.rank is not None:
            return self.rank

        faster_times = Time.objects.filter(map=self.map, type=self.type, stage=self.stage, time__lt=self.time)
        older_equal_times = Time.objects.filter(map=self.map, type=self.type, stage=self.stage, time=self.time, id__lte=self.id)
        return faster_times.count() + older_equal_times.count()


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
