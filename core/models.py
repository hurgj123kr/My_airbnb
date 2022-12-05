from django.db import models
from . import managers

class TimeStampedModel(models.Model):
    """ Time Stampe Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()
    
    # database안에 데이터가 저장되지 않도록 해줌.
    class Meta:
        abstract = True