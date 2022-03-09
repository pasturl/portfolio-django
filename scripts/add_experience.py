from myportfolio import models

#my_model_fields = [field.name for field in models.Project._meta.get_fields()]
b = models.Experience(designation='LEAD DATA SCIENTIST - PRODUCT',
                      start_date='2022-02-01',
                      end_date='2022-03-08',
                      is_present=True,
                      company='Mango',
                      location='Barcelona, Spain',
                      responsibilities_1='Develop a computer vision project, opening a new line of research',
                      responsibilities_2='Define a new project to optimize early product decisions',
                      responsibilities_3='Proof of concept in visual',
                      responsibilities_4='Implement best practices and methodology')
b.save()

b = models.Experience(designation='LEAD DATA SCIENTIST - PRICING',
                      start_date='2020-10-15',
                      end_date='2022-02-01',
                      is_present=False,
                      company='Mango',
                      location='Barcelona, Spain',
                      responsibilities_1='Develop and maintenance of the price optimization platform defining weekly prices at SKU level',
                      responsibilities_2='Desing and improve big data architecture',
                      responsibilities_3='Coordinate the roll-out to new countries and product lines',
                      responsibilities_4='Evaluate and improve ML models and project architecture')
b.save()

b = models.Experience(designation='INNOVATION AREA MANAGER',
                      start_date='2019-01-01',
                      end_date='2020-10-14',
                      is_present=False,
                      company='AIA',
                      location='Barcelona, Spain',
                      responsibilities_1='Manage data science team of +10 members and oversee all activities ensuring alignment with client requirements and company goals',
                      responsibilities_2='Agile implementation of PoC to be used in project proposals',
                      responsibilities_3='Present commercial proposal and negotiate contracts with clients, being key account manager with several clients',
                      responsibilities_4='Wide variety of projects: text mining, forecasting, recommendation systems, anomaly detection, graph analysis, fraud detection, customer segmentation')
b.save()

b = models.Experience(designation='SENIOR DATA SCIENTIST',
                      start_date='2018-02-01',
                      end_date='2018-12-31',
                      is_present=False,
                      company='AIA',
                      location='Barcelona, Spain',
                      responsibilities_1='Develop data science projects independently, interacting and presenting results to clients',
                      responsibilities_2='Help in preparation of PoC',
                      responsibilities_3='Mentoring and coaching of new team members',
                      responsibilities_4='Forecasting project at differente scales (days vs minutes) and algorithms (GBM vs LSTM')
b.save()

b = models.Experience(designation='DATA SCIENTIST',
                      start_date='2017-09-11',
                      end_date='2018-01-31',
                      is_present=False,
                      company='KDP',
                      location='Barcelona, Spain',
                      responsibilities_1='Consultant in projects in financial industry for CaixaBank',
                      responsibilities_2='Participate in a project to optimize price of complex financial assets developing econometric and ML models, and a Montecarlo simulation tool',
                      responsibilities_3='Explore and extract data from complex databases',
                      responsibilities_4='Collaboration in a project of text mining to detect topics in Spark')
b.save()

b = models.Experience(designation='R+D TECHNICAL STAFF',
                      start_date='2017-09-11',
                      end_date='2018-01-31',
                      is_present=False,
                      company='University of A Coruña',
                      location='A Coruña, Spain',
                      responsibilities_1='Develop novel Deep Learning algorithms using Tensorflow and Keras frameworks',
                      responsibilities_2='Researcher in Artificial Intelligence and Neuroscience',
                      responsibilities_3='Writing scientific papers and project proposals',
                      responsibilities_4='Presenting research results in international conferences')
b.save()