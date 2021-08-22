from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import signals

import datetime



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateField(null=True)
    name = models.CharField(max_length=225, null=True)
    last_name = models.CharField( max_length=50, null=True)

    def __str__(self) -> str:
        return 
    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.crearted_date = datetime.date.today()
        if self.last_name:
            self.last_name = self.last_name + f'_{str(self.id)}'
        return super().save(*args, **kwargs)


@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

