import pandas as pd
from django.core.management import BaseCommand
from myportfolio.models import Project


class Command(BaseCommand):
    help = 'Load projects csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path, sep=";")

        for index, row in df.iterrows():
            b = Project(title=row["title"],
                        description=row["description"],
                        github_link=None if row["github_link"] == "nan" else row["github_link"],
                        demo_link=None if row["demo_link"] == "nan" else row["demo_link"],
                        icon=None if row["icon"] == "nan" else row["icon"],
                        keywords=row["keywords"],
                        tech_stack_1=row["tech_stack_1"],
                        tech_stack_2=row["tech_stack_2"],
                        tech_stack_3=row["tech_stack_3"],
                        tech_stack_4=row["tech_stack_4"],
                        image=row["image"])
            print(f'Saving project: {row["title"]}')
            b.save()
