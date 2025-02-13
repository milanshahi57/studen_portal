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


from .models import Notice

def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'notices.html', {'notices': notices})


# for contact form submission
from .models import ContactMessage
from django.contrib import messages


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Save to database
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill out all fields.")

    return render(request, 'contact.html')