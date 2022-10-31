from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    """ Command to Definition """

    help = "This command auto create amenities "

    def add_argument(self, parser):
        parser.add_argument("--number", help="How many data do you want to create")

    def handle(self,*args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Pool",
            "Hot tub",
            "Free parking on premises",
            "EV charger",
            "Crib",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]
        
        for i in amenities:
            Amenity.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS("Amenities created!!"))

