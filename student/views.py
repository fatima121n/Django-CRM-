from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.



def home(request):
    students = Student.objects.all()

    context = {
        'students':students
    }
    
    return render(request, 'home.html', context)
