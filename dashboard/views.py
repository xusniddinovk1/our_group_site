from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from students.models import *


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(main_dashboard)
    return render(request, 'students/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def main_dashboard(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    failed_subjects = StudentSubjectFailure.objects.all()

    ctx = {
        'subjects': len(subjects),
        'teachers': len(teachers),
        'students': len(students),
        'failed_subjects': len(failed_subjects)
    }
    return render(request, 'students/index.html', ctx)
