from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def year(request):
    return render(request, 'year.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Subject  # Make sure to import the Subject model

def subjects(request, year):
    # Fetch the subjects for the given year from the database
    subjects_list = Subject.objects.filter(year=year)
    
    # Render the subjects template with the year and subjects data
    return render(request, 'subjects.html', {
        'year': year,
        'subjects': subjects_list
    })
