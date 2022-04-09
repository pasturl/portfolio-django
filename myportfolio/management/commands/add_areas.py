import pandas as pd
from django.core.management import BaseCommand
from myportfolio.models import Area


class Command(BaseCommand):
    help = 'Load areas csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path, sep=";")

        for index, row in df.iterrows():
            b = Area(name=row["name"],
                     description=row["description"],
                     image=row["image"])
            print(f'Saving area: {row["name"]}')
            b.save()
