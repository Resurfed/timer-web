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

    def actual_rank(self):
        """
        :return: the exact rank value of the time.

        This is the reliable way to determine a time's rank, as the
        database column for rank is meant solely for filtering top times.
        """
        if self.rank is not None:
            return self.rank

        faster_times = Time.objects.filter(
            map=self.map,
            type=self.type,
            stage=self.stage,
            time__lt=self.time
        )

        older_equal_times = Time.objects.filter(
            map=self.map,
            type=self.type,
            stage=self.stage,
            time=self.time,
            date_updated__lte=self.date_updated
        )

        return faster_times.count() + older_equal_times.count()

    def update_rank_cache(self, limit=10):
        """
        :param limit: The number of top rank values to store as cache.
        The rank cache is only required for ease of access to top times.
        """

        if self.actual_rank() > limit:
            return

        # clear existing ranks.
        Time.objects.all().filter(
            map=self.map,
            type=self.type,
            stage=self.stage,
            rank__isnull=0
        ).update(rank=None)

        # reset ranks.
        times = Time.objects.all().filter(
            map=self.map,
            type=self.type,
            stage=self.stage
        )
        
        times = times.order_by('time', '-date_updated')[:limit]

        for index, time in enumerate(times):
            time.rank = index + 1
            super(Time, time).save()

    def save(self, *args, **kwarg):
        """
        Automatically update rank column on save.
        """
        super(Time, self).save(args, kwarg)
        self.update_rank_cache()

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
