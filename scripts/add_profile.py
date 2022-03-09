from myportfolio import models

#my_model_fields = [field.name for field in models.Profile._meta.get_fields()]
b = models.Profile(name='Lucas Pastur',
                   designation='Lead Data Scientist',
                   summary='Lead Data Scientist with +5 years of professional experience'
                           ' developing cross-industry solutions to'
                           'solve complex problems using machine learning techniques.'
                           ' Manage data scientists teams and lead '
                           'projects end-to-end: develop proof of concepts,'
                           ' oversaw technical implementation and code quality, and '
                           'supervise execution in production environment.',
                   image='lucas.jpg',
                   phone_number='+34 615 200 371',
                   email='lucas.pastur@gmail.com',
                   github_link='https://github.com/pasturl',
                   linkedin_link='https://www.linkedin.com/in/lucas-pastur-romay/')
b.save()
