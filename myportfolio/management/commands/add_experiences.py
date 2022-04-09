import pandas as pd
from django.core.management import BaseCommand
from myportfolio.models import Experience


class Command(BaseCommand):
    help = 'Load experiences csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path, sep=";", encoding='latin1')

        for index, row in df.iterrows():
            b = Experience(designation=row["designation"],
                           start_date=row["start_date"],
                           end_date=row["end_date"],
                           is_present=row["is_present"],
                           company=row["company"],
                           company_url=row["company_url"],
                           location=row["location"],
                           responsibilities_1=row["responsibilities_1"],
                           responsibilities_2=row["responsibilities_2"],
                           responsibilities_3=row["responsibilities_3"],
                           responsibilities_4=row["responsibilities_4"])
            print(f'Saving experience: {row["designation"]}')
            b.save()
