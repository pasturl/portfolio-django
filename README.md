# portfolio-django


``` 
pip install -r requirements.txt
python manage.py makemigrations myportfolio
python manage.py migrate
python manage.py inspectdb 
python manage.py createsuperuser
python manage.py runserver 
python3 manage.py runserver 0.0.0.0:8000
python manage.py shell

python manage.py add_profile --path data/profile.csv
python manage.py add_areas --path data/areas.csv
python manage.py add_experiences --path data/experiences.csv
python manage.py add_academic --path data/academic.csv
python manage.py add_skills --path data/skills.csv
python manage.py add_projects --path data/projects.csv

```