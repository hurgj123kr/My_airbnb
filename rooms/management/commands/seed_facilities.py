from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    """ Command to Definition """

    help = "This command auto create amenities "

    # def add_argument(self, parser):
    #     parser.add_argument("--number", help="How many data do you want to create")

    def handle(self,*args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!!"))

