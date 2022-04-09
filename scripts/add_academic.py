from myportfolio import models

#my_model_fields = [field.name for field in models.Project._meta.get_fields()]
b = models.Academic(designation='Ph.D in Information and Communication Technologies, Faculty of Computer Science.',
                      start_date='2018-05-01',
                      end_date='2014-09-01',
                      is_present=True,
                      university='Universidade da Coruna',
                      location='A Coruna, Spain',
                      responsibilities_1='Thesis Cum Laude. Models of information processing in the brain applied to connectionist Systems. Artificial NeuroGlial Network and Deep Learning',
                      responsibilities_2='',
                      responsibilities_3='',
                      responsibilities_4='')
b.save()

b = models.Academic(designation='Master Degree in Neuroscience',
                      start_date='2014-06-01',
                      end_date='2013-09-01',
                      is_present=False,
                      university='Universidade da Coruna',
                      location='A Coruna, Spain',
                      responsibilities_1='Develop ',
                      responsibilities_2='',
                      responsibilities_3='',
                      responsibilities_4='')
b.save()

b = models.Academic(designation='Degree in Biology',
                      start_date='2013-06-01',
                      end_date='2008-09-01',
                      is_present=False,
                      university='Universidade da Coruna',
                      location='A Coruna, Spain',
                      responsibilities_1='Develop ',
                      responsibilities_2='',
                      responsibilities_3='',
                      responsibilities_4='')
b.save()
