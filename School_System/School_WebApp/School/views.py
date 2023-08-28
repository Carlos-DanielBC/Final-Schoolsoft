from django.shortcuts import render,redirect, get_object_or_404
from .models import Students,Teachers,Parents,Subject,Course,Inscription
from django.http import HttpResponse
from django.db import IntegrityError
from django.template import loader
from School.forms import *
from School.models import *
from django.urls import reverse


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
#---------crear curso, asignatura y estudiante-------------
def Creacion(request):
    return render(request, 'teachers/courses.html')
    
def lista_curso(request):
    # Supongamos que tienes el ID del maestro que quieres consultar
    teacher_id = 1  # Reemplaza con el ID del maestro que deseas consultar

    # Encuentra todas las relaciones del maestro con cursos
    relationships = Relationship.objects.filter(Teachers_id=teacher_id)

    cursos_del_maestro = []  # Lista para almacenar los cursos del maestro con estudiantes

    if relationships.exists():
        for relationship in relationships:
            subject = relationship.Subject_id
            cursos = subject.course_set.all()

            for curso in cursos:
                # Obtener las inscripciones para este curso
                inscriptions = Inscription.objects.filter(course_id=curso)
                students = [inscription.student_id for inscription in inscriptions]
                cursos_del_maestro.append({
                    'curso': curso,
                    'students': students,
                    'asignatura': subject.name  # Agregar el nombre de la asignatura
                })

    return render(request, 'teachers/courses.html', {'cursos': cursos_del_maestro})


def calificar(request):
    try:
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        # print(student_id+' '+student_name)
        if not student_id:
            # Si no se recibe student_id en POST, tomarlo de la sesión
            student_id = request.session.get('student_id')
            
        if not student_name:
            # Si no se recibe student_name en POST, tomarlo de la sesión
            student_name = request.session.get('student_name')
        
        request.session.pop('student_id', None)
        request.session.pop('student_name', None)
        
        student = get_object_or_404(Students, id=student_id)
        inscriptions = Inscription.objects.filter(student_id=student)
        cursos_y_asignaturas = []
        
        for inscription in inscriptions:
            course = inscription.course_id
            subject = course.subject_id
            cursos_y_asignaturas.append({'course': course, 'subject': subject})
            
        return render(request, 'teachers/calification.html', {'student': student, 'cursos_y_asignaturas': cursos_y_asignaturas})
    except Exception as e:
        return redirect('teachers')

def califications(request):
    if request.method == 'POST':
        
        asignatura_id = request.POST.get('asignatura_id')
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        
        request.session['student_id'] = student_id
        request.session['student_name'] = student_name
        
        if 'button1' in request.POST:
            p1 = request.POST.get('p1')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'firstPeriod': p1}
            )
            
            if not created:
                calificacion_obj.firstPeriod = p1
                calificacion_obj.save()
            return redirect('calificar')
        
        elif 'button2' in request.POST:
            p2 = request.POST.get('p2')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p2}
            )
            
            if not created:
                calificacion_obj.secondPeriod = p2
                calificacion_obj.save()
            return redirect('calificar')
        
        elif 'button3' in request.POST:
            p3 = request.POST.get('p3')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p3}
            )
            
            if not created:
                calificacion_obj.thirdPeriod = p3
                calificacion_obj.save()
            return redirect('calificar')
        
        elif 'button4' in request.POST:
            p4 = request.POST.get('p4')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p4}
            )
            
            if not created:
                calificacion_obj.fourthPeriod = p4
                calificacion_obj.save()
            return redirect('calificar')
        
        elif 'button5' in request.POST:
            p5 = request.POST.get('p5')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p5}
            )
            
            if not created:
                calificacion_obj.finish = p5
                calificacion_obj.save()
            return redirect('calificar')
        
    return redirect('calificar')
