from myportfolio import models
import pandas as pd

df = pd.read_csv("profile.csv", sep=";")

for index, row in df.iterrows():
    b = models.Profile(name=row["name"],
                       designation=row["designation"],
                       summary=row["summary"],
                       image=row["image"],
                       email=row["email"],
                       github_link=row["github_link"],
                       linkedin_link=row["linkedin_link"])
    print("Saving b")
    b.save()
