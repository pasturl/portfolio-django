from myportfolio import models

b = models.Skill(name='Python',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg')
b.save()

b = models.Skill(name='PySpark',
                 image='https://alansimpson.me/python/cheatsheets/pysparkrdd/pysparkrdd256.jpg')
b.save()

b = models.Skill(name='R',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg')
b.save()

b = models.Skill(name='Tensorflow',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original-wordmark.svg')
b.save()

b = models.Skill(name='Docker',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain-wordmark.svg')
b.save()

b = models.Skill(name='AWS',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg')
b.save()

b = models.Skill(name='MongoDB',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original-wordmark.svg')
b.save()

b = models.Skill(name='Git',
                 image='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original-wordmark.svg')
b.save()
