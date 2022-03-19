from myportfolio import models

#my_model_fields = [field.name for field in models.Project._meta.get_fields()]
b = models.Project(title=' PhD Thesis and research papers',
                   description='PhD and scientific papers in Artificial Intelligence and Neuroscience',
                   github_link='https://scholar.google.es/citations?user=ZMOI-J0AAAAJ&hl=es',
                   keywords='Artificial Intelligence; Neuroscience;',
                   tech_stack_1='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg',
                   tech_stack_2='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original-wordmark.svg',
                   tech_stack_3='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-plain.svg',
                   tech_stack_4='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg',
                   image='ai.jfif')
b.save()

b = models.Project(title='Sign language translator',
                   description='Application to real-time translation sign language to text',
                   github_link='https://github.com/pasturl/sign-language',
                   keywords='Computer Vision; Video classification;',
                   tech_stack_1='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg',
                   tech_stack_2='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original-wordmark.svg',
                   tech_stack_3='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg',
                   tech_stack_4='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg',
                   image='sign.jpg')
b.save()

b = models.Project(title='Sentiment analysis',
                   description='Sentiment analysis using Machine Learning models (BERT, LightGBM, Logistic Regression)',
                   github_link='https://github.com/pasturl/Sentiment-Analysis',
                   keywords='Natural Language Processing; Artificial Neural Networks; Transformers;',
                   tech_stack_1='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg',
                   tech_stack_2='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original-wordmark.svg',
                   tech_stack_3='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg',
                   tech_stack_4='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg',
                   image='wordcloud_sentiment.png')
b.save()

