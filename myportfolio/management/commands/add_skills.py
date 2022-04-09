import pandas as pd
from django.core.management import BaseCommand
from myportfolio.models import Skill


class Command(BaseCommand):
    help = 'Load skills csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path, sep=";")

        for index, row in df.iterrows():
            b = Skill(name=row["name"],
                      image=row["image"])
            print(f'Saving skill: {row["name"]}')
            b.save()
