"""
URL configuration for School_WebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from School import views

urlpatterns = [
    path('School/', include('School.urls')),
    path('admin/', admin.site.urls),
    path('all-professors/', views.all_professors, name='all-professors'),
    path('add-students/', views.add_students, name='add-students'),
    path('home/', views.index, name='home'),
    path('edit-student/',views.edit_student,name='edit-student'),
    path("edit-student/<int:id>",views.edit_st,name="edit-student"),
    path("edit-student/update/<int:id>",views.edit_st_confirm,name="update"),
    path('add-courses/',views.add_courses, name='add-courses'),
    path('edit-courses/', views.edit_courses, name='edit-courses'),
    path('edit-courses/<int:id>', views.edit_courses_b, name='edit-courses'),
    path('edit-courses/update/<int:id>', views.edit_courses_confirm, name='update'),
    path('add-subjects/',views.add_subjects,name='add-subjects'),
    path('edit-subjects/',views.edit_subjects,name='edit-subjects'),
    path('edit-subjects/<int:id>',views.edit_subjects_b,name='edit-subjects'),
    path('edit-subjects/update/<int:id>',views.edit_subjects_confirm,name='update'),
    path('teachers/', views.teachers),
    path('courses/', views.lista_curso),
    path('calificar/', views.calificar, name='calificar'),
    path('calification/', views.califications, name='calification'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='School/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)