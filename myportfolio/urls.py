from django.urls import path

from . import views


urlpatterns =[

    path("",views.index,name="index"),
    path("projects",views.projects,name="projects"),
    path("experiences",views.experiences,name="experiences"),
    path("academic",views.academic,name="academic"),
    path("blogs",views.blogs,name="blogs"),
    path("contact",views.contact,name="contact"),
    path("resume", views.resume, name="resume")

]