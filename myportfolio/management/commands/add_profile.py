import pandas as pd
from django.core.management import BaseCommand
from myportfolio.models import Profile


class Command(BaseCommand):
    help = 'Load profile csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path, sep=";")

        for index, row in df.iterrows():
            b = Profile(name=row["name"],
                        designation=row["designation"],
                        summary=row["summary"],
                        image=row["image"],
                        email=row["email"],
                        github_link=row["github_link"],
                        linkedin_link=row["linkedin_link"])
            print(f'Saving profile: {row["name"]}')
            b.save()
