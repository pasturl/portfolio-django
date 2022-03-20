from myportfolio import models

b = models.Area(name='Bussiness',
                description='Leading product squad in a fashion retail company. Experience in a wide industries workin as consultant.',
                image='bussiness.png')
b.save()

b = models.Area(name='Big Data',
                description='Develop and mantain data science projects in Big Data enviroments',
                image='big_data.png')
b.save()

b = models.Area(name='Artificial Intelligence',
                description='Expertise in wide industries',
                image='ai_ann.png')
b.save()