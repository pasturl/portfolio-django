from myportfolio import models

#my_model_fields = [field.name for field in models.Project._meta.get_fields()]
b = models.Project(title='Research papers',
                   description='Scientific papers in Artificial Intelligence and Neuroscience',
                   github_link='https://scholar.google.es/citations?user=ZMOI-J0AAAAJ&hl=es',
                   tech_stack='Python',
                   image='Research papers')
b.save()

b = models.Project(title='Sign language translator',
                   description='Application to real-time translation sign language to text',
                   github_link='https://github.com/pasturl/sign-language',
                   tech_stack='Python',
                   image='Research papers')
b.save()

b = models.Project(title='Sentiment analysis',
                   description='Sentiment analysis using Machine Learning models (BERT, LightGBM, Logistic Regression)',
                   github_link='https://github.com/pasturl/Sentiment-Analysis',
                   tech_stack='Python',
                   image='Research papers')
b.save()

