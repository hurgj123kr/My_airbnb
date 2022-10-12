from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item Definition """

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    """ RoomType Definition """
    
    pass


class Amenity(AbstractItem):
    """ Amenity Definition """
    
    pass


class Facility(AbstractItem):
    """ Facility Definition """
    
    pass


class HouseRule(AbstractItem):
    """ House Rule Definition """
    
    pass


class Room(core_models.TimeStampedModel):

    """ Room Models Definition """
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=35)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    #모든 이름을 사용자의 이름으로 넣는것.
    def __str__(self):
        return self.name



    
