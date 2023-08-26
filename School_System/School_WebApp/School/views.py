from django.shortcuts import render,redirect
from .models import Students,Teachers,Parents,Subject,Course,Inscription
from django.http import HttpResponse
from django.template import loader
from School.forms import *
from School.models import *
def index(request):
    latest_inscriptions_list = Inscription.objects.order_by("-date_inscription")[:5]
    template = loader.get_template("school/index.html")
    context = {
        "latest_inscriptions_list": latest_inscriptions_list,
    }
    
    return HttpResponse(template.render(context,request))

def all_professors(request):
    return render(request,'School/all-professors.html')


def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = CourseForm()
    return render(request,'School/add-courses.html',{'form': form})


def add_subjects(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/add-subjects')
            except:
                pass
    else:
        form = SubjectForm()
    return render(request,'School/add-library.html',{'form': form,'courses': courses})

def add_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = StudentForm
    return render(request,'School/add-student.html',{'form': form})

def edit_student(request):
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students})

def edit_subjects(request):
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects})


def edit_courses(request):
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses})

def edit_st(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students,'students_v':students_v})

def edit_subjects_b(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})

def edit_courses_b(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses,'courses_v':courses_v})

def edit_courses_confirm(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    form = CourseForm(request.POST, instance=courses_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-courses')
    return render(request,template,{'courses':courses,'courses_v':courses_v})

def edit_subjects_confirm(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    form = SubjectForm(request.POST, instance=subjects_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-subjects')
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})


def edit_st_confirm(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    form = StudentForm(request.POST,instance=students_v)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/home')
    return render(request,template,{'students':students,'students_v':students_v})


#----------teacher-------------
def teachers(request):
    return render(request, 'teachers/teachers.html')
