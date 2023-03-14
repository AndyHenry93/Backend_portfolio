from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import *
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.
def index(request):
    about = About.objects.get(id=1)
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()
    testimonals = Testimonal.objects.all()

    if request.method == "POST":
        email_form = ContactForm(request.POST)
        if email_form.is_valid():
            cd = email_form.cleaned_data
            email = cd['email']
            subject = "Portfolio message: " + ","+cd['subject']
            message = cd['message']
            try:
                send_mail(subject,message,email,['Andy.henry1223@gmail.com'])
                messages.success(request,'Email Sucessfully Sent, Thank You.')
            except BadHeaderError:
                messages.error(request,'Email Unsucessfully Sent, please check the form.')
                return HttpResponse("Invalid header found.")
            return redirect("/")
    else:
        email_form = ContactForm()

    context = {
        'about': about,
        'skill': skills,
        'education':education,
        'experience': experience,
        'project': projects,
        'testimonal':testimonals, 
        'email_form':email_form
    }
    return render(request,'resume/index.html',context)

def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project':project 
    }
    return render(request,'resume/detail.html',context)

def success(request):
    return HttpResponse("Success! Thank you for your message.")



