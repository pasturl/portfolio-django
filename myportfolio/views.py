from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill, Connection,Experience,Profile,Area,Academic
# Create your views here.
from .forms import NameForm
from django.core.mail import send_mail
from os import listdir
from os.path import isfile, join


MAX_EXPERIENCE = 10
def index(request):
    template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:MAX_EXPERIENCE]
    academic = Academic.objects.all().order_by('-start_date')[:MAX_EXPERIENCE]
    profile = Profile.objects.all().first()
    areas = Area.objects.all()
    form = NameForm()
    context = {'projects': projects, 'form': form,'experiences':experiences,'academic':academic,'profile':profile,'areas':areas}
    return HttpResponse(template.render(context, request))


def experiences(request):
    return HttpResponse("you are in experience page")


def academic(request):
    return HttpResponse("you are in academic page")


def ai_art_gallery(request):
    template = loader.get_template("myportfolio/ai_art_gallery.html")
    ai_art_gallery_img_path = "myportfolio/static/img/ai_art_gallery"
    paints_paths = [f for f in listdir(ai_art_gallery_img_path) if isfile(join(ai_art_gallery_img_path, f))]
    paints_paths.sort()
    context = {'paints': paints_paths}
    return HttpResponse(template.render(context, request))


def blogs(request):
    template = loader.get_template("myportfolio/blog.html")
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        template = loader.get_template("myportfolio/contact.html")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ob = Connection()
            ob.your_name = form.cleaned_data['your_name']
            ob.email = form.cleaned_data['email']
            ob.subject = form.cleaned_data['subject']
            ob.message = form.cleaned_data['message']
            ob.save()
            context={}
            return HttpResponse(template.render(context, request))
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return HttpResponseRedirect('/myportfolio')


def projects(request):
    template = loader.get_template("myportfolio/projects.html")
    projects = Project.objects.all()
    context = {'projects': projects}
    return HttpResponse(template.render(context, request))


def resume(request):
    template = loader.get_template("myportfolio/resume.html")
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:MAX_EXPERIENCE]
    academic = Academic.objects.all().order_by('-start_date')[:MAX_EXPERIENCE]
    context = {'skills': skills, 'experiences': experiences, 'academic': academic}
    return HttpResponse(template.render(context, request))
