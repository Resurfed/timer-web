from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    steam_id = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=32, blank=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    def __str__(self):
        return "%s (%s)" % (self.name, self.steam_id)


class PlayerOption(models.Model):
    player = models.OneToOneField(Player, primary_key=True, on_delete=models.CASCADE)
    hud_config = models.CharField(max_length=30, blank=True)
    hide_panel = models.BooleanField()
    sounds = models.BooleanField()
    color_scheme = models.SmallIntegerField()
    chat_mode = models.SmallIntegerField()
    teleport_velocity = models.BooleanField()
