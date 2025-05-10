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
    return render(request, 'dashboard/login.html')


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
    return render(request, 'dashboard/index.html', ctx)


@login_required_decorator
def subjects_list(request):
    subjects = Subject.objects.all()
    ctx = {
        'subjects': subjects
    }
    return render(request, 'dashboard/subjects/list.html', ctx)


@login_required_decorator
def create_subject(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subjects_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/subjects/form.html', ctx)


@login_required_decorator
def update_subject(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subjects_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/subjects/form.html', ctx)


@login_required_decorator
def delete_subject(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subjects_list')


################ Teacher ####################
@login_required_decorator
def teachers_list(request):
    teachers = Teacher.objects.all()
    ctx = {
        'teachers': teachers
    }
    return render(request, 'dashboard/teachers/list.html', ctx)


@login_required_decorator
def create_teacher(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/teachers/form.html', ctx)


@login_required_decorator
def update_teacher(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/teachers/form.html', ctx)


@login_required_decorator
def delete_teacher(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teachers_list')


############## Student ###################
@login_required_decorator
def students_list(request):
    students = Student.objects.all()
    ctx = {
        'students': students
    }
    return render(request, 'dashboard/students/list.html', ctx)


@login_required_decorator
def create_student(request):
    model = Student()
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/students/form.html', ctx)


@login_required_decorator
def update_student(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/students/form.html', ctx)


@login_required_decorator
def delete_student(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('students_list')


################# failed_subject ############
@login_required_decorator
def failed_subjects_list(request):
    failed_subjects = StudentSubjectFailure.objects.all()
    ctx = {
        'failed_subjects': failed_subjects
    }
    return render(request, 'dashboard/failed_subjects/list.html', ctx)


@login_required_decorator
def create_failed_subject(request):
    model = StudentSubjectFailure()
    form = StudentSubjectFailureForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('failed_subjects_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/failed_subjects/form.html', ctx)


@login_required_decorator
def update_failed_subject(request, pk):
    model = StudentSubjectFailure.objects.get(pk=pk)
    form = StudentSubjectFailureForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('failed_subjects_list')
    ctx = {
        'model': model,
        'form': form
    }

    return render(request, 'dashboard/failed_subjects/form.html', ctx)


@login_required_decorator
def delete_failed_subject(request, pk):
    model = StudentSubjectFailure.objects.get(pk=pk)
    model.delete()
    return redirect('failed_subjects_list')
