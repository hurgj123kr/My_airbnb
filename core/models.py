from django.db import models

class TimeStampedModel(models.Model):
    """ Time Stampe Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()
    
    # database안에 데이터가 저장되지 않도록 해줌.
    class Meta:
        abstract = True