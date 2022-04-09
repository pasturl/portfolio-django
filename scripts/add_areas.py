from myportfolio import models

b = models.Area(name='Artificial Intelligence',
                description='Expertise in wide industries',
                image='ai_ann.png')
b.save()

b = models.Area(name='Big Data',
                description='Develop and mantain data science projects in Big Data enviroments using PySpark, AWS and Airflow.',
                image='big_data.png')
b.save()

b = models.Area(name='Bussiness',
                description='Leading product squad in a fashion retail company. Experience in a wide industries working as consultant.',
                image='bussiness.png')
b.save()

b = models.Area(name='Programming',
                description='Experience implementing software, maintaining it and reviewing code.',
                image='programming.png')
b.save()

b = models.Area(name='Visualization',
                description='Analyze and process data to prepare visualization and dashboards.',
                image='visualization.png')
b.save()

b = models.Area(name='Neuroscience',
                description='Background in Neuroscience and Biology, great interest apply Machine Learning algorithms in healthcare problems.',
                image='neuroscience.png')
b.save()