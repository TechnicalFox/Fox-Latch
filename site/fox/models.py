from django.db import models
from django.contrib.auth.models import User

class Fox(models.Model):
    user = models.OneToOneField(User)
    ip = models.GenericIPAddressField(protocol='IPv4')

    def __unicode__(self):
        return self.ip
