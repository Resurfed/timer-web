from .models import Time
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
@receiver(post_save, sender=Time)
def save_time(sender, instance, created, **kwargs):
    if instance.actual_rank() <= 10 and instance.rank is None:
        update_time_ranks(instance, 10)
'''