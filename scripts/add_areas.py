from myportfolio import models

b = models.Area(name='Bussiness',
                description='Expertise in wide industries',
                image='collect.svg')
b.save()

b = models.Area(name='Big Data',
                description='Expertise in wide industries',
                image='process.svg')
b.save()

b = models.Area(name='Artificial Intelligence',
                description='Expertise in wide industries',
                image='visualise.svg')
b.save()