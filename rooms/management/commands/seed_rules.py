from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    """ Command to Definition """

    help = "This command auto create rules "

    def add_argument(self, parser):
        parser.add_argument("--number", help="How many data do you want to create")

    def handle(self,*args, **options):
        rules = [
            "No loud noise after 11 pm",
            "No food or drinks in bedrooms",
            "No parties or events",
            "No smoking",
            "No pets / Pets allowed",
        ]
        
        for r in rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS("Houserules created!!"))

