from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    """ Command to Definition """

    help = "This command auto create roomtypes "

    def add_argument(self, parser):
        parser.add_argument("--number", help="How many data do you want to create")

    def handle(self,*args, **options):
        types = [
            "Entire place",
            "Private rooms",
            "Hotel rooms",
            "Shared rooms",
        ]
        
        for t in types:
            RoomType.objects.create(name=t)
        self.stdout.write(self.style.SUCCESS("RoomType created!!"))

