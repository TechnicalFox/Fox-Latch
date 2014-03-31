from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Fox(models.Model):
    user = models.OneToOneField(User)
    ip = '0.0.0.0' #models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)

    def __unicode__(self):
        return self.ip

# create user object to attach to fox object
def create_fox_user_callback(sender, instance, **kwargs):
    fox, new = Fox.objects.get_or_create(user=instance)
post_save.connect(create_fox_user_callback, User)
